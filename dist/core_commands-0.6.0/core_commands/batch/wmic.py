from ..bin._batch import _batch

def wmic(arguments):
    if arguments:
        return command_cmd(f"wmic {arguments}")
    return command_cmd("wmic")