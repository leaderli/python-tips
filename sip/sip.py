import getopt
import os
import sys

from config import Config
from git import Git
from li import li_log
from li.li_cmd import LiCmd

config = Config()

git = Git()


class Sip(LiCmd):

    def do_config(self, argv):
        """ """
        config.onecmd(argv)

    def do_env(self, argv):
        """ get environment variable , same as printenv"""
        if args:
            print('{}={}'.format(argv, os.environ.get(argv)))
        else:
            print(os.environ)
            for k, v in os.environ.items():
                print('{}={}'.format(k, v))

    def do_exit(self, argv):
        """exit the program."""
        print("bye.")
        exit(0)

    def do_pwd(self, argv):
        """ get sip.py directory"""

        print(os.path)
        print(os.getcwd())

    def do_git(self, argv):
        """ """
        git.onecmd(argv)

    def help_config(self, argv):

        print(argv)
        config.do_help(None)


if __name__ == '__main__':
    args = sys.argv[1:]
    short_opts = "d"
    long_opts = ["debug"]

    opts = getopt.getopt(args, short_opts, long_opts)[0]

    for opt, param in opts:
        if opt in ('-d', '--debug'):
            li_log.set_debug()
            args.remove(opt)

    sip = Sip()
    sip.prompt = '> '
    command = ' '.join(args)
    if command:
        sip.onecmd(command)
    else:
        # noinspection PyTypeChecker
        sip.do_help(None)
        sip.cmdloop()
