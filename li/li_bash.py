import logging
import subprocess
from subprocess import Popen, PIPE

from li.li_decorator import log_args


@log_args
def run(command):
    subprocess.run(command, shell=True, universal_newlines=True)


@log_args
def call(command):
    with Popen(command, shell=True, stdout=PIPE, stderr=PIPE, universal_newlines=True) as fd:
        out, err = fd.communicate()
        if fd.returncode:
            raise Exception(err.strip())
        logging.debug(out.strip())
        return out.strip()


def ssh_call(address, workdir, command):
    return call(
        """ssh -q {address}  'cd {workdir} && {command}'""".format(address=address, workdir=workdir, command=command))
