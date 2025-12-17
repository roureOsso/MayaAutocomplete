# -*- coding: utf-8 -*-
import io
import sys
import os
import os.path as path
import re
import zipfile
from functools import partial

from urllib.request import urlretrieve

TYPES_TABLE = {"bool()": ["boolean"],
               "int()": ["uint", "int", "int64"],
               "float()": ["linear", "float", "angle", "time"],
               "str()": ["string", "name", "script"],
               "tuple()": ["floatrange", "timerange"]}

# Doc download page
# https://knowledge.autodesk.com/support/maya/troubleshooting/caas/downloads/content/download-install-maya-product-help.html
# Devkit download page
# https://aps.autodesk.com/developer/overview/maya

DOWNLOAD_SOURCES = {
    "MayaHelp": {
        "2023": "https://download.autodesk.com/akn/2023/maya/autodesk-maya-user-guide-2023.3-en.zip",
        "2022": "https://download.autodesk.com/us/support/maya_user_guide/2022.2/autodesk_maya_user_guide_2022.2_htm_ade_2.1_en.zip",
        "2020": "https://download.autodesk.com/us/support/maya_user_guide/2020/autodesk-maya-user-guide-2020.htm-ade-2.1.en.zip",
        "2019": "https://download.autodesk.com/us/support/maya_2019/maya-2019-user-guide_enu_offline.zip",
        "2018": "https://download.autodesk.com/us/support/files/maya_help_2018/MayaHelp2018_enu.zip",
    },

    "DevKit": {  # There is no point making difference between windows and linux when it comes to maya commands
        "2026": "https://autodesk-adn-transfer.s3.us-west-2.amazonaws.com/ADN+Extranet/M%26E/Maya/devkit+2026/Autodesk_Maya_2026_3_Update_DEVKIT_Windows.zip",
        "2025": "https://autodesk-adn-transfer.s3.us-west-2.amazonaws.com/ADN+Extranet/M%26E/Maya/devkit+2025/Autodesk_Maya_2025_3_Update_DEVKIT_Windows.zip",
        "2024": "https://autodesk-adn-transfer.s3-us-west-2.amazonaws.com/ADN+Extranet/M%26E/Maya/devkit+2024/Autodesk_Maya_2024_2_Update_DEVKIT_Windows.zip",
    }
}


class MayaDocParser:

    def __init__(self):
        self._maya_version = ""
        self._build_path = ""

    def build(self):
        self.__get_build_path()
        self.__get_maya_version()

        # Download the Maya documentation (might be in the MayaHelp or devkit depending on the version)
        source = "MayaHelp" if self._maya_version in DOWNLOAD_SOURCES["MayaHelp"] else "DevKit"
        doc_download_path = DOWNLOAD_SOURCES[source][self._maya_version]

        doc_temp_zip = urlretrieve(
            url=doc_download_path, reporthook=partial(self._retrieve_progress, prefix="Doc download"))[0]
        zip_doc = zipfile.ZipFile(doc_temp_zip)

        # Docs inside the devKit for the latest Maya version ar inside a nested zip
        if source == "DevKit":
            nested_zip = [f for f in zip_doc.namelist() if f.endswith("docs.zip")][0]
            nested_zip_data = io.BytesIO(zip_doc.read(nested_zip))
            zip_doc = zipfile.ZipFile(nested_zip_data)

        commands_files = [f for f in zip_doc.namelist() if path.dirname(f) == "CommandsPython" and f.endswith(".html")]

        # region -> Create directories for the autocomplete, parse the docs and write them down.
        maya_stubs_path = path.join(self._build_path, "autoCompleteMaya" + self._maya_version, "maya-stubs")
        ac_path = path.join(maya_stubs_path, "cmds")
        os.makedirs(ac_path)

        files_to_create = [path.join(maya_stubs_path, "__init__.pyi"), path.join(ac_path, "__init__.pyi")]

        for file_path in files_to_create:
            with open(file_path, "w"):
                pass

        with open(path.join(ac_path, "__init__.pyi"), "w+") as commands_file:
            for i, command_file in enumerate(commands_files):
                self._retrieve_progress(
                    block_count=i + 1, block_size=1, total_size=len(commands_files), prefix="Autocomplete build")

                command_hdl = zip_doc.open(command_file)
                command_content = command_hdl.read()
                command_name = path.basename(command_file).replace(".html", "")
                command_def = self._parse_documentation(command=command_name, command_content=command_content)

                if command_def:
                    commands_file.write(command_def)

                command_hdl.close()
        # endregion

        print("Auto complete ready! \n"
              "It is recommended to open the __init__ file and auto reformat the code for easier future reading")

    def __get_build_path(self):
        print("A new autoComplete will be generated, please, indicate where it should be located")
        self._build_path = input("AC path:")

        if not path.exists(self._build_path):
            print("ERROR: No such file or directory, try again\n")
            self.__get_build_path()

    def __get_maya_version(self):

        self._maya_version = input("Maya version:")
        versions = list(DOWNLOAD_SOURCES["MayaHelp"].keys()) + list(DOWNLOAD_SOURCES["DevKit"].keys())
        if self._maya_version not in versions:
            versions.sort()
            print(f"Documentation not listed for version - {self._maya_version} -\n"
                  f"Available major versions -> {versions}\n")

            self.__get_maya_version()

    @staticmethod
    def _parse_documentation(command, command_content):

        # Force string type to be python 3.x compatible
        command_content = str(command_content)
        c_index = command_content.find(command + "(")

        # If any command si described continue
        if c_index == -1:
            return

        start = c_index + len(command) + 1

        # Each command has a synopsis with the command being called and all the flag have their type
        synopsis_str = command_content[start:command_content.find(")", start)]

        arguments_types = list()
        for arguments in re.findall("\[<(.*?)>]", synopsis_str):
            # Get all occurrences between ">" and "<", these will be the flags and its types
            arg_and_type = re.findall(">(.*?)<", arguments)[::2]
            if not arg_and_type:
                continue

            arg = arg_and_type[0]
            short_arg = re.findall("<code><b>{}</b>\(<b>(.*?)</b>\)".format(arg), command_content)[0]
            arg_type = None

            # If an argument has '[' or ']' in it, it is a list type
            if "[" in arg_and_type[1] and "]" in arg_and_type[1]:
                arg_type = "list"

            # If it is not a list, find the correct type in the types table
            else:
                for key, values in TYPES_TABLE.items():
                    if arg_and_type[1] in values:
                        arg_type = key
                        break

            if not arg_and_type:
                raise RuntimeError("arg type is not a list and is not defined in the table, contact who did this")

            arguments_types.append("=".join([arg, arg_type]))

            if short_arg and not short_arg == arg:
                arguments_types.append("=".join([short_arg, arg_type]))

        arguments_types.extend(["*args", "**kwargs"])

        command_def = f"def {command}({', '.join(arguments_types)}):\n    pass\n\n"

        return command_def

    @staticmethod
    def _retrieve_progress(block_count, block_size, total_size, prefix):
        """
        Create and update a progress bar within an iteration process.
        :param block_count: int // current block being downloaded
        :param block_size: int // size of the blocks being downloaded (bytes)
        :param total_size: str // total size to be downloaded (bytes)
        :param prefix: str // bit added before the loading bar
        """
        max_iteration = round(total_size / float(block_size))
        percents = "{:.1f}".format(100 * (block_count / float(max_iteration)))
        filled_length = int(round(75 * block_count / float(max_iteration)))
        bar = "█" * filled_length + "▯" * (75 - filled_length)

        sys.stdout.write(f"\r{prefix}: |{bar}| {percents}%"),

        if block_count == max_iteration:
            sys.stdout.write("\n")
        # Make sure that the string is not being buffered
        sys.stdout.flush()


if __name__ == "__main__":
    py_parser = MayaDocParser()
    py_parser.build()
