import logging
import os
import re
import sys
from datetime import datetime

from li import li_log
from li.li_bash import call, run
from li.li_cmd import LiCmd
from li.li_getopt import short_opts_exits


def complete_keys(keys, prefix):
    return [k for k in keys if k.startswith(prefix)]


class Sip(LiCmd):

    def do_config(self, argv):
        """ """
        pass

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

    def do_pull(self, argv):
        """
        更新脚本至最新脚本，使用 git 命令是实现的

        -b 更新前自动备份，备份使用当前的 commit 摘要
        """

        run('git fetch --all')
        status = call('git diff origin/HEAD --stat')

        if not status:
            print('no change from origin')
            return
        if short_opts_exits(argv, 'b'):
            sha = call('git rev-parse --short HEAD')
            run('cd .. && zip -r {name}.{sha}.zip {name}'.format(name='python-tips', sha=sha))
        run('git reset --hard HEAD')
        run('git pull')
        exit()

    def do_push(self, argv):
        """
        上传最新脚本,实际使用 git 进线推送。 参数作为 commit 的 信息，默认使用当前时间。

        """

        msg = argv
        if not msg:
            now = datetime.now()  # current date and time
            msg = now.strftime("%Y%m%d  %H%M%S")

        status = call('git status -s')

        if status:
            import platform

            if platform.system() == 'Windows':
                run('git add .')
                run('git commit -m "{}"'.format(msg))
                run('git push')
            else:
                cmd = '''
                        git add .  &&
                        git commit -m "{}"  &&
                        git push
                      '''.format(msg)
                run(cmd)

    def complete_debug(self, text, line, begin_idx, end_idx):
       
        return complete_keys(('-i',), text)

    def complete_env(self, text, line, begin_idx, end_idx):

        return complete_keys(os.environ.keys(), text)


if __name__ == '__main__':

    sip = Sip()

    os.chdir(re.sub(r'sip/sip.py$', '', __file__))
    sip.prompt = '> '

    args = sys.argv[1:]
    # -d 直接进入debug模式
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
