from ..bin._batch import _batch

def curl(arguments,url):
    """
    Transfer data from or to a server, using one of the supported protocols (HTTP, HTTPS, FTP, FTPS, SCP, SFTP, TFTP, DICT, TELNET, LDAP or FILE). 
    """
    command = f"curl {arguments} {url}"
    return command_cmd(command)