import sys
from pathlib import Path


def is_python3():
    assert sys.version_info.major == 3, 'only support python 3'


def is_exist_dir(path):
    d = Path(path)
    assert d.exists() and d.is_dir(), path + ' is not a exist directory'
