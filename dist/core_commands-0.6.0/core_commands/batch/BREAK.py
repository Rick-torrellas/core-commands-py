from ..bin._batch import _batch

def BREAK(rest = False):
    if rest:
        return command_cmd(f"break {rest}")
    return command_cmd("break")