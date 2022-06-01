import logging
from subprocess import Popen, PIPE


def bash(command):
    logging.debug(command)
    with Popen(command, shell=True, stdout=PIPE, stderr=PIPE, universal_newlines=True) as fd:
        out, err = fd.communicate()
        if err:
            raise Exception(err.strip())
        return out.strip()
