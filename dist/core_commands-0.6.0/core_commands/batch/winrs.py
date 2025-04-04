from ..bin._batch import _batch

def winrs(arguments):
    if(arguments):
        return command_cmd(f"winrs {arguments}")
    return command_cmd("winrs")