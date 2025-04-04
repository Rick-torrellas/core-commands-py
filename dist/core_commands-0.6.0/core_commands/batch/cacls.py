from ..bin._batch import _batch

def cacls(pathname,arguments = False):
    if arguments:
        return command_cmd(f"cacls {pathname} {arguments}")
    return command_cmd(f"cacls {pathname}")