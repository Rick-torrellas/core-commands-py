from ._validate import _validateArguments
from subprocess import run

def noShell(command,arguments):
    if _validateArguments(arguments):
        return run([command,arguments],
                    capture_output=True,
                    text=True
                    )
    return run([command],
                    capture_output=True,
                    text=True
                    )