from ..bin._batch import _batch

def wecutil(arguments):
    command_base = f"wecutil"
    return command_cmd(f"{command_base} {arguments}")