from ..bin._batch import _batch

def hostname(arguments = False):
    if(arguments):
        return command_cmd(f"hostname {arguments}")
    return command_cmd("hostname")
