from ..bin._batch import _batch

def dir(pathname,arguments,options={
    "debug": False
}):
    if(pathname):
        command_cmd(f"dir {pathname} {arguments}")