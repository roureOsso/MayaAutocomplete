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
             'int': ['uint', 'int', 'time'],
             'float': ['linear', 'float', 'angle'],
             'str': ['string', 'name', 'script', 'timerange']}

# toDo: some flags are weird I will check them
weird_flags = ['time', 'angle', 'timerange']

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
        for arguments in synopsis_str.split('],'):
            # Get all occurrences between ">" and "<", these will be the flags and its types
            arg_and_type = re.findall('>(.*?)<', arguments)[::2]
            if not arg_and_type:
                continue

            # toDo: I need to get the shorter version
            arg = arg_and_type[0]
            arg_type = None

            if '[' in arg_and_type[1] and ']' in arg_and_type[1]:
                arg_type = 'list'
            else:
                # toDo: remove this check once all is solved
                if arg_and_type[1] in weird_flags:
                    print('command: {}, flag={}, type={}'.format(command, arg, arg_and_type[1]))

                for key, values in arg_types.items():
                    if arg_and_type[1] in values:
                        arg_type = key

            if not arg_type:
                # toDo: try to solve problem knowing the flags type
                print command
                print arg
                print arg_and_type[1]
                raise Exception

            arguments_types.append([arg, arg_type])
