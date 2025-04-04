from ..bin._validate import _validateArguments,_validateCommand
from subprocess import run
from ..bin.exceptions import UnknownCommand

def shell(command):
    if _validateCommand(command):
        raise UnknownCommand(command)
    return run([command],
                    capture_output=True,
                    text=True,
                    shell=True
                    )