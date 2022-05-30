from subprocess import Popen, PIPE


def bash(command: str):
    with Popen(command, shell=True, stdout=PIPE, stderr=PIPE, universal_newlines=True) as fd:
        return fd.stdout.read()
