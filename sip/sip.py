import os
import sys

from config import Config
from git import Git
from li.li_cmd import LiCmd

config = Config()

git = Git()


class Sip(LiCmd):

    def do_config(self, args: str):
        """ """
        config.onecmd(args)

    def do_env(self, args):
        """ get environment variable , same as printenv"""
        if args:
            print('{}={}'.format(args, os.environ.get(args)))
        else:
            print(os.environ)
            for k, v in os.environ.items():
                print('{}={}'.format(k, v))

    def do_exit(self, args):
        """exit the program."""
        print("bye.")
        exit(0)

    def do_git(self, args):
        """ """
        git.onecmd(args)


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
