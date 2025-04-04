from ..bin._batch import _batch

def bcdedit(arguments = False):
    if arguments:
        return command_cmd(f"bcdedit {arguments}")
    return command_cmd(f"bcdedit")