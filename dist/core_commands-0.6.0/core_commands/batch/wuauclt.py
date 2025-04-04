from ..bin._batch import _batch

def wuauclt(arguments = False):
    if arguments:
        return command_cmd(f'wuauclt {arguments}')
    return command_cmd('wuauclt')