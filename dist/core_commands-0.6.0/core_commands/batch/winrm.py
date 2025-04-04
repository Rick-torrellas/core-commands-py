from ..bin._batch import _batch

def winrm(arguments):
    if arguments:
        return command_cmd(f"winrm {arguments}")
    return command_cmd("winrm")