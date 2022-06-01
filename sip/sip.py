import getopt
import os
import sys
from datetime import datetime

from config import Config
from git import Git
from li import li_log
from li.li_bash import run
from li.li_cmd import LiCmd

config = Config()

git = Git()


class Sip(LiCmd):

    def do_config(self, argv):
        """ """
        config.onecmd(argv)

    def do_env(self, argv):
        """
        get environment variable , same as printenv
        if give a key , it will return the specific environment variable value
        """
        if argv:
            val = os.environ.get(argv)
            if val:
                print('{}={}'.format(argv, val))
        else:
            for k, v in os.environ.items():
                print('{}={}'.format(k, v))

    def do_exit(self, argv):
        """exit the program."""
        print("bye.")
        exit(0)

    def do_pwd(self, argv):
        """ get sip.py absolute path """
        print(__file__)

    def do_git(self, argv):
        """ """
        git.onecmd(argv)

    def do_push(self, argv):
        """
        上传最新脚本,实际使用 git 进线推送。 参数作为 commit 的 信息，默认使用当前时间。

        """

        msg = argv
        if not msg:
            now = datetime.now()  # current date and time
            msg = now.strftime("%m/%d/%Y, %H:%M:%S")

        cmd = '''
                git add . &&
                git commit -m '{}' &&
                git push
              '''.format(msg)

        print(run('git status -s '))
        print(run(cmd))


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
        if sip.onecmd(command):
            sip.cmdloop()
    else:
        sip.cmdloop()
