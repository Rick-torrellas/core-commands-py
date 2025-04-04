from ..bin._batch import _batch

def winget(command,options = False):
    if(options):
        return command_cmd(f"winget {command} {options}")
    return command_cmd(f"winget {command}")