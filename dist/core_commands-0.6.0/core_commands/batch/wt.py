from ..bin._batch import _batch

def wt(commandParameter,arguments):
    command_base = f"wt"
    if(commandParameter):
        if(arguments):
            return command_cmd(f"{command_base} {arguments} {commandParameter}")
        return command_cmd(f"{command_base} {commandParameter}")
    return command_cmd(command_base)