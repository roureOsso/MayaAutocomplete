import maya.cmds as mc
import types
import keyword

with open(r'C:\Users\roure\Downloads\__init__.py', 'w+') as commands_file:
    for command in dir(mc):
        if not isinstance(getattr(mc, command), types.BuiltinFunctionType):
            continue
        try:
            help_string = mc.help(command, syntaxOnly=True)
        except RuntimeError:
            continue

        if "Flags:\n" not in help_string:
            command_line = """
def {}(*args, **kwargs):
    pass
""".format(command)
        else:
            args = list()
            for arg in help_string.split(' '):
                if not arg or not len(arg.strip()) > 1 or not '-' == arg[0]:
                    continue
                arg = arg.strip()[1:]

                if arg in ['e', 'edit', 'q', 'query'] or keyword.iskeyword(arg):
                    continue

                args.append(arg)
            # toDo: if not args (because only query and edit are known) use the other command_line format
            command_line = """
def {}({}*args, **kwargs):
    pass
""".format(command, '=None, '.join(args) + '=None, ')
        commands_file.write(command_line)
