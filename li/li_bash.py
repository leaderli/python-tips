import logging
from subprocess import Popen, PIPE


def bash(command):
    print('111111111111111111')
    logging.debug(command)
    with Popen(command, shell=True, stdout=PIPE, stderr=PIPE, universal_newlines=True) as fd:
        out, err = fd.communicate()
        print(out)
        print(err)
        if err:
            raise Exception(err.strip())
        return out.strip()
