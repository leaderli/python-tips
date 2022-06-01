import logging
import os
import sys
from datetime import datetime

from config import Config
from git import Git
from li import li_log
from li.li_bash import run, call
from li.li_cmd import LiCmd
from li.li_getopt import short_opts_exits

config = Config()

git = Git()


class Sip(LiCmd):

    def do_config(self, argv):
        """ """
        config.onecmd(argv)

    def do_debug(self, argv):
        """
        日志级别调整为 DEBUG , 提示符更改为 #
        -i 将日志级别调整为INFO ,提示符更改为 >
        """
        if short_opts_exits(argv, 'i'):
            li_log.set_format()
            sip.prompt = '> '
        else:
            li_log.set_format(logging.DEBUG)
            sip.prompt = '# '

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

    def do_pull(self, argv):
        """
        更新脚本，会自动备份当前脚本，并强制下载最新脚本，需要在配置文件中配置 git 地址，配置项key为git 。
        仅支持使用ssh，需要自己去设定免密相关
        """
        sha = call('git rev-parse --short HEAD')

        pass

    def do_push(self, argv):
        """
        上传最新脚本,实际使用 git 进线推送。 参数作为 commit 的 信息，默认使用当前时间。

        """

        msg = argv
        if not msg:
            now = datetime.now()  # current date and time
            msg = now.strftime("%m/%d/%Y, %H:%M:%S")

        cmd = 'git status -s'

        status = call(cmd)

        if status:
            # cmd = '''
            #         git add . &&
            #         git commit -m '{}' &&
            #         git push
            #       '''.format(msg)
            # call(cmd)
            run('git add . ')
            run("git commit -m   'test'")
            run('git push ')


if __name__ == '__main__':

    sip = Sip()
    
    sip.prompt = '> '

    args = sys.argv[1:]
    opt = short_opts_exits(args, 'd')
    if opt:
        sip.do_debug('')
        args.remove(opt)

    command = ' '.join(args)
    if command:
        if sip.onecmd(command):
            sip.cmdloop()
    else:
        sip.cmdloop()
