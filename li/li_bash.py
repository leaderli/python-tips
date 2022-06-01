import logging
from subprocess import Popen, PIPE


def run(command):
    logging.debug(command)
    with Popen(command, shell=True, stdout=PIPE, stderr=PIPE, universal_newlines=True) as fd:
        out, err = fd.communicate()
        if fd.returncode:
            raise Exception(err.strip())
        print(out.strip())


def call(command):
    logging.debug(command)
    with Popen(command, shell=True, stdout=PIPE, stderr=PIPE, universal_newlines=True) as fd:
        out, err = fd.communicate()
        if fd.returncode:
            raise Exception(err.strip())
        return out.strip()
