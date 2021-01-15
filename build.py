import sys
import os
import os.path as path
import re
import webbrowser
import zipfile

# Make this code compatible with python2 and python3
if sys.version_info >= (3, 0):
    u_input = input
else:
    u_input = raw_input

TYPES_TABLE = {'bool()': ['boolean'],
               'int()': ['uint', 'int', 'int64'],
               'float()': ['linear', 'float', 'angle', 'time'],
               'str()': ['string', 'name', 'script'],
               'tuple()': ['floatrange', 'timerange']}

# Download page
# https://knowledge.autodesk.com/support/maya/troubleshooting/caas/downloads/content/download-install-maya-product-help.html

documentation_versions = {
    '2020.4': 'https://download.autodesk.com/us/support/maya_user_guide/2020/autodesk-maya-user-guide-2020-5-htm-ade-2.1-en.zip',
    '2020.3': 'https://download.autodesk.com/us/support/maya_user_guide/2020/autodesk-maya-user-guide-2020-4-htm-ade-2.1-en.zip',
    '2020.2': 'https://download.autodesk.com/us/support/maya_user_guide/2020/autodesk-maya-user-guide-2020.2-htm-ade-2.1-en.zip',
    '2020.1': 'https://download.autodesk.com/us/support/maya_user_guide/2020/autodesk-maya-user-guide-2020.1.htm-ade-2.1.enu.zip',
    '2020': 'https://download.autodesk.com/us/support/maya_user_guide/2020/autodesk-maya-user-guide-2020.htm-ade-2.1.en.zip',

    '2019.3': 'https://help.autodesk.com/view/MAYAUL/2019/ENU/?guid=Maya_ReleaseNotes_2019_3_release_notes_html',
    '2019.2': 'https://download.autodesk.com/us/support/maya_2019.2/maya-2019.2-user-guide_enu_offline.zip',
    '2019.1': 'https://download.autodesk.com/us/support/maya_2019/maya-2019.1-user-guide_enu_offline.zip',
    '2019': 'https://download.autodesk.com/us/support/maya_2019/maya-2019-user-guide_enu_offline.zip',

    '2018.4': 'https://download.autodesk.com/us/support/files/maya_2018.4_update/MayaHelp2018_4_Update_enu.zip',
    '2018.3': 'https://download.autodesk.com/us/support/files/maya_2018.3_update/MayaHelp2018_3_Update_enu.zip',
    '2018.2': 'https://download.autodesk.com/us/support/files/maya_2018.2_update/MayaHelp2018_2_Update_enu.zip',
    '2018': 'https://download.autodesk.com/us/support/files/maya_help_2018/MayaHelp2018_enu.zip',

    '2017': 'https://download.autodesk.com/us/support/files/maya_help_enu_2017/MayaHelp2017_enu.zip',

    '2016': 'https://download.autodesk.com/us/support/files/maya_2016/MayaHelp2016_enu.zip'
}


def run():
    def get_user_info():
        """
        Get all the used needed info.
        :return: str // documentation path
        """
        download_doc = u_input('Do you want to download the Maya documentation? Y/N:')
        if download_doc == 'N':
            documentation_path = u_input('Input the Maya documentation folder:')
        elif download_doc == 'Y':
            def get_maya_version():
                version = u_input('Maya documentation version to download:')
                if version not in documentation_versions.keys():
                    available_versions = list(documentation_versions.keys())
                    available_versions.sort()
                    print('Documentation not listed for version - {} -\n'
                          'Available versions -> {}'
                          'NOTE: You can also download the files by your self.'.format(version, available_versions))

                    version = get_maya_version()

                return version

            maya_version = get_maya_version()
            print('INFO: Accept the download in your desired folder and wait for the download to finish')
            webbrowser.open(documentation_versions[maya_version])

            zip_path = u_input('Zip path:')
            documentation_path = path.join(path.split(zip_path)[0], 'mayaDoc' + maya_version)

            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(documentation_path)

        else:
            print('Please set Y or N')
            documentation_path = get_user_info()

        return documentation_path

    doc_path = get_user_info()
    if 'CommandsPython' not in os.listdir(doc_path):
        raise RuntimeError('The specified folder does not contain "CommandsPython" folder')

    commands_path = path.join(doc_path, 'CommandsPython')
    print('INFO: The -> __init__.py <- file is about to be written choose the correct directory or move it later')
    init_path = u_input('Set the path were the __init__.py will be saved or overwrite:')

    print('Writing commands...')
    with open(path.join(init_path, '__init__.py'), 'w+') as commands_file:
        for command_file in os.listdir(commands_path):
            command = command_file.replace('.html', '')
            file_path = path.join(commands_path, command_file)
            # if not path.isfile(file_path) or '_' in command or '.' in command:
            if not path.isfile(file_path):
                continue

            with open(file_path, 'r') as doc_handle:
                doc = doc_handle.read()
                c_index = doc.find(command + '(')
                # If any command si described continue
                if c_index == -1:
                    continue

                start = c_index + len(command) + 1

                # Each command has a synopsis with the command being called and all the flag have their type
                synopsis_str = doc[start:doc.find(')', start)]

                arguments_types = list()
                for arguments in re.findall('\[<(.*?)>]', synopsis_str):
                    # Get all occurrences between ">" and "<", these will be the flags and its types
                    arg_and_type = re.findall('>(.*?)<', arguments)[::2]
                    if not arg_and_type:
                        continue

                    arg = arg_and_type[0]
                    short_arg = re.findall('<code><b>{}</b>\(<b>(.*?)</b>\)'.format(arg), doc)[0]
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

                commands_file.write(
                    "def {}({}*args, **kwargs):\n    pass\n\n".format(command, ', '.join(arguments_types)))

    print('Command autocomplete file DONE!')
    print('INFO: It is recommended to open the __init__ file and reformat the code')


if __name__ == "__main__":
    run()
