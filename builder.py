import maya.cmds as mc
import maya.mel as mel


for command in dir(mc):
    help_string = str(mel.eval('help("{}")'.format(command)))
    if "No Flags" in help_string:
        continue
    # toDo: extract the string following the "-" caracter
    
    command_line = """
def {}(, *args, **kwargs):
    pass
""".format(command)
    
    # open an write the new command to the end of the file.

