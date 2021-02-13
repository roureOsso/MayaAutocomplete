# -*- coding: utf-8 -*-

import sys
import os
import os.path as path
import platform
import re
import zipfile
import shutil
from functools import partial

# Make this code compatible with python2 and python3
if sys.version_info >= (3, 0):
    from urllib.request import urlretrieve
    u_input = input

else:
    from urllib import urlretrieve
    u_input = raw_input

TYPES_TABLE = {'bool()': ['boolean'],
               'int()': ['uint', 'int', 'int64'],
               'float()': ['linear', 'float', 'angle', 'time'],
               'str()': ['string', 'name', 'script'],
               'tuple()': ['floatrange', 'timerange']}

# Doc download page
# https://knowledge.autodesk.com/support/maya/troubleshooting/caas/downloads/content/download-install-maya-product-help.html
DOWNLOAD_SOURCES = {
    "MayaHelp": {
        "2020": "https://download.autodesk.com/us/support/maya_user_guide/2020/autodesk-maya-user-guide-2020.htm-ade-2.1.en.zip",
        "2019": "https://download.autodesk.com/us/support/maya_2019/maya-2019-user-guide_enu_offline.zip",
        "2018": "https://download.autodesk.com/us/support/files/maya_help_2018/MayaHelp2018_enu.zip",
        "2017": "https://download.autodesk.com/us/support/files/maya_help_enu_2017/MayaHelp2017_enu.zip",
        "2016": "https://download.autodesk.com/us/support/files/maya_2016/MayaHelp2016_enu.zip"
    },
    "DevKit": {
        "Windows": {
            "2020": "https://autodesk-adn-transfer.s3.us-west-2.amazonaws.com/ADN%20Extranet/M%26E/Maya/devkit%202020/Autodesk_Maya_2020_DEVKIT_Windows_Hotfix_1.zip",
            "2019": "https://s3-us-west-2.amazonaws.com/autodesk-adn-transfer/ADN+Extranet/M%26E/Maya/devkit+2019/Autodesk_Maya_2019_DEVKIT_Windows.zip",
            "2018": "https://s3-us-west-2.amazonaws.com/autodesk-adn-transfer/ADN+Extranet/M%26E/Maya/devkit+2018/Maya2018-DEVKIT_Windows.zip",
            "2017": "https://s3-us-west-2.amazonaws.com/autodesk-adn-transfer/ADN+Extranet/M%26E/Maya/devkit+2017/Maya2017_DEVKIT_Windows.zip",
            "2016": "https://s3-us-west-2.amazonaws.com/autodesk-adn-transfer/ADN+Extranet/M%26E/Maya/devkit+2016/Maya2016_DEVKIT_Windows.zip"
        },
        "Linux": {
            "2020": "https://autodesk-adn-transfer.s3.us-west-2.amazonaws.com/ADN%20Extranet/M%26E/Maya/devkit%202020/Autodesk_Maya_2020_DEVKIT_Linux_Hotfix_1.tgz",
            "2019": "https://s3-us-west-2.amazonaws.com/autodesk-adn-transfer/ADN+Extranet/M%26E/Maya/devkit+2019/Autodesk_Maya_2019_DEVKIT_Linux.tgz",
            "2018": "https://s3-us-west-2.amazonaws.com/autodesk-adn-transfer/ADN+Extranet/M%26E/Maya/devkit+2018/Maya2018_DEVKIT_Linux.tgz",
            "2017": "https://s3-us-west-2.amazonaws.com/autodesk-adn-transfer/ADN+Extranet/M%26E/Maya/devkit+2017/Maya2017_DEVKIT_Linux.tgz",
            "2016": "https://s3-us-west-2.amazonaws.com/autodesk-adn-transfer/ADN+Extranet/M%26E/Maya/devkit+2016/Maya2016_DEVKIT_Linux.zip"
        }
    }
}


class MayaDocParser(object):

    def __init__(self):
        super(MayaDocParser, self).__init__()

        self._maya_version = None
        self._build_path = None

    def build(self, custom_build=False):
        """
        Will create the new autoComplete, you can choose between an automatic setup and a custom one.
        For the custom build you will be asked to provide the Maya Documentation to parse.
        :param custom_build: bool //
        """
        self.__get_maya_version()
        self.__get_build_path()

        if custom_build:
            self._custom_setup()

        else:
            self._auto_setup()
            print('Auto complete DONE!! Find it where you said :D')

    def _auto_setup(self):
        """
        Will downlad everything is needed, parse the new documentation and release a new python autoComplete
        """

        # Download the Maya documentation
        doc_download_path = DOWNLOAD_SOURCES['MayaHelp'][self._maya_version]
        doc_temp_zip = urlretrieve(
            url=doc_download_path, reporthook=partial(self.__retrieve_progress, prefix='Doc download'))[0]
        zip_doc = zipfile.ZipFile(doc_temp_zip)

        # Download the MayaDevkit
        dev_kit_download_path = DOWNLOAD_SOURCES['DevKit'][platform.system()][self._maya_version]
        dev_kit_temp_zip = urlretrieve(
            url=dev_kit_download_path, reporthook=partial(self.__retrieve_progress, prefix='devKit download'))[0]

        ac_path = path.join(self._build_path, 'py' + self._maya_version)
        zip_devkit = zipfile.ZipFile(dev_kit_temp_zip)

        for dev_file in zip_devkit.namelist():
            if dev_file.startswith('devkitBase/devkit/other/pymel/extras/completion/py'):
                zip_devkit.extract(dev_file, self._build_path)

        shutil.move(
            path.join(self._build_path, 'devkitBase', 'devkit', 'other', 'pymel', 'extras', 'completion', 'py'),
            ac_path)

        shutil.rmtree(path.join(self._build_path, 'devkitBase'))

        commands_files = [
            f for f in zip_doc.namelist() if path.dirname(f) == 'CommandsPython' and f.endswith('.html')]

        with open(path.join(ac_path, 'maya', 'cmds', '__init__.py'), 'w+') as commands_file:
            for i, command_file in enumerate(commands_files):
                self.__retrieve_progress(
                    block_count=i + 1, block_size=1, total_size=len(commands_files), prefix='Autocomplete build')

                command_hdl = zip_doc.open(command_file)
                command_content = command_hdl.read()
                command_name = path.basename(command_file).replace('.html', '')
                command_def = self.__parse_documentation(command=command_name, command_content=command_content)

                if command_def:
                    commands_file.write(command_def)

                command_hdl.close()

    def _custom_setup(self):
        print('Custom build not implemented yet')

    @staticmethod
    def __retrieve_progress(block_count, block_size, total_size, prefix):
        """
        Create and update a progress bar within an iteration process.
        :param block_count: int // current block being downloaded
        :param block_size: int // size of the blocks being downloaded (bytes)
        :param total_size: str // total size to be downloaded (bytes)
        :param prefix: str // bit added before the the loading bar
        """
        max_iteration = round(total_size / float(block_size))
        percents = "{:.1f}".format(100 * (block_count / float(max_iteration)))
        filled_length = int(round(75 * block_count / float(max_iteration)))
        bar = '█' * filled_length + '▯' * (75 - filled_length)

        sys.stdout.write('\r{}: |{}| {}%'.format(prefix, bar, percents)),

        if block_count == max_iteration:
            sys.stdout.write('\n')
        # Make sure that the string is not being buffered
        sys.stdout.flush()

    def __get_maya_version(self):
        """
        Get the maya documentation version to download
        """

        self._maya_version = u_input('Maya version:')

        if self._maya_version not in DOWNLOAD_SOURCES['MayaHelp'].keys():
            available_versions = list(DOWNLOAD_SOURCES['MayaHelp'].keys())
            available_versions.sort()
            print('Documentation not listed for version - {} -\n'
                  'Available major versions -> {}\n'
                  'NOTE: For other options choose the custom build\n'.format(self._maya_version, available_versions))

            self.__get_maya_version()

    def __get_build_path(self):
        """
        A new pyAutocomplete will be generated, here I'm getting the path where it should be stored.
        """
        print('A new autoComplete will be generated, please, indicate where it should be located')
        self._build_path = u_input('AC path:')

        if not path.exists(self._build_path):
            print('ERROR: No such file or directory, try again\n')
            self.__get_build_path()

        if 'devkitBase' in os.listdir(self._build_path):
            print('ERROR: "devkitBase" folder found in the given dir')
            self.__get_build_path()

    @staticmethod
    def __parse_documentation(command, command_content):

        # Force string type to be python 3.x compatible
        command_content = str(command_content)
        c_index = command_content.find(command + '(')

        # If any command si described continue
        if c_index == -1:
            return

        start = c_index + len(command) + 1

        # Each command has a synopsis with the command being called and all the flag have their type
        synopsis_str = command_content[start:command_content.find(')', start)]

        arguments_types = list()
        for arguments in re.findall('\[<(.*?)>]', synopsis_str):
            # Get all occurrences between ">" and "<", these will be the flags and its types
            arg_and_type = re.findall('>(.*?)<', arguments)[::2]
            if not arg_and_type:
                continue

            arg = arg_and_type[0]
            short_arg = re.findall('<code><b>{}</b>\(<b>(.*?)</b>\)'.format(arg), command_content)[0]
            arg_type = None

            # If an argument has '[' or ']' in it, it is a list type
            if '[' in arg_and_type[1] and ']' in arg_and_type[1]:
                arg_type = 'list'

            # If it is not a list, find the correct type in the types table
            else:
                for key, values in TYPES_TABLE.items():
                    if arg_and_type[1] in values:
                        arg_type = key
                        break

            if not arg_and_type:
                raise RuntimeError(
                    'arg type is not a list and is not defined in the table, contact who did this')

            arguments_types.append('='.join([arg, arg_type]))

            if short_arg and not short_arg == arg:
                arguments_types.append('='.join([short_arg, arg_type]))

        arguments_types.extend(['*args', '**kwargs'])

        command_def = "def {}({}):\n    pass\n\n".format(command, ', '.join(arguments_types))

        return command_def


if __name__ == "__main__":

    py_parser = MayaDocParser()

    build_type = u_input('Run custom build? Maya Help and Devkit will be requested. Y/N:')

    if build_type in ['Y', 'N']:
        py_parser.build(custom_build=True if build_type == 'Y' else False)

    else:
        raise ValueError('Please set Y or N')
