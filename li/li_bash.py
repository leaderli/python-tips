from subprocess import Popen, PIPE


def bash(command: str):
    with Popen(command, shell=True, stdout=PIPE, stderr=PIPE, universal_newlines=True) as fd:
        if fd.returncode != 0:
            raise RuntimeError(fd.stderr.read())
        return fd.stdout.read()
