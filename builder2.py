import sys
import os
import os.path as path
import re
import types
import keyword

# Make this code compatible with python2 and python3
if sys.version_info >= (3, 0):
    doc_path = input('Input the Maya documentation folder:')
else:
    doc_path = raw_input('Input the Maya documentation folder:')

if 'CommandsPython' not in os.listdir(doc_path):
    raise RuntimeError('The specified folder does not contain "CommandsPython" folder')

commands_path = path.join(doc_path, 'CommandsPython')

arg_types = {'bool': ['boolean'],
             'int': ['uint', 'int', 'int64'],
             'float': ['linear', 'float', 'angle', 'time'],
             'str': ['string', 'name', 'script'],
             'tuple': ['floatrange', 'timerange']}

auto_complete = ''
for command_file in os.listdir(commands_path):
    command = command_file.replace('.html', '')
    file_path = path.join(commands_path, command_file)
    if not path.isfile(file_path):
        continue

    with open(file_path, 'r') as doc_handle:
        doc = doc_handle.read()
        start = doc.find(command + '(') + len(command) + 1
        end = doc.find(')', start)

        # Each command has a synopsis with the command being called and all the flag have their type
        synopsis_str = doc[start:end]

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
                for key, values in arg_types.items():
                    if arg_and_type[1] in values:
                        arg_type = key
                        break

            if not arg_and_type:
                raise RuntimeError('The arg type is not a list and is not defined in the table, contact who did this')

            arguments_types.extend([[arg, arg_type], [short_arg, arg_type]])
