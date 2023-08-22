if __name__ == "__main__":
    from command_cmd import command_cmd
else:
    from .command_cmd import command_cmd
from pathlib import PurePath

def mkdir(destination = False,obtions = False,debug=False):
    if (debug):
        print(destination,obtions)
    if (destination):
        destination = PurePath(destination)
        return command_cmd(f'mkdir {destination}',obtions)
    return False

mkdir('./vagina')