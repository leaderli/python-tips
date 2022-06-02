import logging
import os
import re
import sys
from datetime import datetime

import yaml
from li import li_log
from li.li_bash import call, run
from li.li_cmd import LiCmd
from li.li_getopt import single_short_opts_exits

SIP_CONFIG_FILES = 'SIP_CONFIG_FILES'


def complete_keys(keys, prefix):
    return [k for k in keys if k.startswith(prefix)]


class Sip(LiCmd):

    def __init__(self):
        super().__init__()

        self.__config = {}

        config_files = os.environ.get(SIP_CONFIG_FILES) or []
        if config_files:
            config_files = config_files.split(',')
        config_files.insert(0, 'sip.yaml')

        for config_file in config_files:
            # 相对路径地址
            if not config_file.startswith("/"):
                config_file = os.path.join(os.getcwd(), 'sip', config_file)
            with open(config_file) as f:
                self.__config.update(yaml.load(f.read(), Loader=yaml.Loader))

        pass

    def do_config(self, argv):
        """
        查看当前环境的配置项，不同环境的配置文件可通过配置环境变量 SIP_CONFIG_FILES来设定环境相关的配置文件，环境相关的配置文件可指定多个，靠后的配置项覆盖前面的

         可指定多个参数，查找指定key的值，
        """

        argv = argv.split()
        argv.reverse()
        d = self.__config

        while argv:
            key = argv.pop()
            d = d.get(key, {})

        print(d)

    def do_debug(self, argv):
        """
        日志级别调整为 DEBUG , 提示符更改为 #

         -i 将日志级别调整为INFO ,提示符更改为 >
        """
        if single_short_opts_exits(argv, 'i'):
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
        """
        脚本的根目录，即该脚本的绝对路径 去除sip/sip.py后
        """
        print(os.getcwd())

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
        if single_short_opts_exits(argv, 'b'):
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

    def complete_config(self, text, line, begin_idx, end_idx):

        keys = line.split()

        # 去头去尾
        keys.pop()
        keys.reverse()

        d = self.__config
        #
        while keys:
            key = keys.pop()
            d = d.get(key, {})

        return [k for k in d.keys() if k.startswith(text)]

    def complete_debug(self, text, line, begin_idx, end_idx):

        return complete_keys(('-i',), text)

    def complete_env(self, text, line, begin_idx, end_idx):

        return complete_keys(os.environ.keys(), text)


if __name__ == '__main__':

    os.chdir(re.sub(r'sip/sip.py$', '', __file__))

    sip = Sip()

    sip.prompt = '> '

    args = sys.argv[1:]
    # -d 直接进入debug模式
    opt = single_short_opts_exits(args, 'd')
    if single_short_opts_exits(args, 'd'):
        sip.do_debug('')
        args.remove(opt)

    command = ' '.join(args)
    if command:
        if sip.onecmd(command):
            sip.cmdloop()
    else:
        sip.cmdloop()
