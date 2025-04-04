from platform import system

def command(command,arguments):
    if system() == "Windows":
        return baxh(command,arguments)
    return bazh(command,arguments)