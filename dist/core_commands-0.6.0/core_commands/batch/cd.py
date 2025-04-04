from ..bin._batch import _batch

def cd(pathname,arguments = False):
    """
    Change Directory - Select a Folder (and drive)
    """
    command_cmd(f"cd {arguments} {pathname}")