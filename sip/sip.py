import os
import sys

from config import config
from li.li_cmd import LiCmd


class Sip(LiCmd):

    def do_config(self, key: str):
        """ """
        config.onecmd(key)

    def do_env(self, key):
        """ get environment variable , same as printenv"""
        if key:
            print('{}={}'.format(key, os.environ.get(key)))
        else:
            print(os.environ)
            for k, v in os.environ.items():
                print('{}={}'.format(k, v))

    def do_exit(self, args):
        """exit the program."""
        print("bye.")
        exit(0)


if __name__ == '__main__':
    sip = Sip()
    sip.prompt = '> '
    command = ' '.join(sys.argv[1:])
    if command:
        sip.onecmd(command)
    else:
        # noinspection PyTypeChecker
        sip.do_help(None)
        sip.cmdloop()
