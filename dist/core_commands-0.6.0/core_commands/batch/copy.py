from ..bin._batch import _batch

def copy(source,destination,sourceArguments = "",destinationArguments = ""):
    command = f"copy {source} {sourceArguments} {destination} {destinationArguments}"
    return command_cmd(command)