from ..bin._batch import _batch

def verify(onOff):
    if (onOff):
        return command_cmd(f"verify {onOff}")
    return command_cmd("verify")
