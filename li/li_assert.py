import sys


def is_python3():
    assert sys.version_info.major == 3, 'only support python 3'
