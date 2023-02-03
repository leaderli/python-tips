import logging
import os
import re
import sys
from datetime import datetime

import yaml
from li import li_decorator, li_assert
from li import li_log
from li.li_bash import call, run
from li.li_cmd import LiCmd
from li.li_decorator import run_on_uat
from li.li_getopt import single_short_opts_exits
from li.li_util import deep_get

SIP_CONFIG_FILES = 'SIP_CONFIG_FILES'
SIP_ENV = 'sip_env'


def complete_keys(line, keys, prefix):
    input_keys = line.split()
    del input_keys[0]
    # 最后输入的是 - 则 提示补全的为所有 - 开头的命令

    if input_keys and input_keys[-1] == '-':
        return list(map(lambda k: k.replace('-', ''),
                        [k for k in keys if k.startswith('-') and k not in input_keys]))
    else:
        return [k for k in keys if k.startswith(prefix) and k not in input_keys]


class Sip(LiCmd):

    def __init__(self):
        super().__init__()

        self.__config = {}

        config_files = os.environ.get(SIP_CONFIG_FILES)
        if config_files:
            config_files = config_files.split(',')
        else:
            config_files = []
        config_files.insert(0, 'sip.yaml')

        for config_file in config_files:
            # 相对路径地址
            if not config_file.startswith("/"):
                config_file = os.path.join(os.getcwd(), 'sip', config_file)
            with open(config_file) as f:
                self.__config.update(yaml.load(f.read(), Loader=yaml.Loader))

        super().__log__(li_log.get_logger('sip', deep_get(self.__config, ['sip', 'log']) or 'sip.log'))
        pass

    def do_backup(self, argv):
        """ 备份war包，默认备份为zip包，zip包以当天时间戳加上自增编号"""
        backup_origin = deep_get(self.__config, ['backup', 'origin'])
        backup_target = deep_get(self.__config, ['backup', 'target'])
        li_assert.is_exist_dir(backup_origin)
        li_assert.is_exist_dir(backup_target)
        apps = argv.split()

        logging.debug('prepare backup ' + str(apps))

        if not apps:
            print('no app to backup')
            return

        today = datetime.now().strftime('backup_%Y%m%d_')
        num = len([z for z in os.listdir(backup_target) if z.endswith('.zip')]) + 1
        backup_zip_name = today + str(num).zfill(3)
        logging.debug('backup ' + backup_zip_name)
        pass

    def do_config(self, argv):
        """
        查看当前环境的配置项，不同环境的配置文件可通过配置环境变量 SIP_CONFIG_FILES 来设定环境相关的配置文件，环境相关的配置文件可指定多个，靠后的配置项覆盖前面的

         可指定多个参数，查找指定key的值，
        """

        argv = argv.split()
        d = self.__config
        d = deep_get(d, argv)
        print(yaml.dump(d))

    def do_debug(self, argv):
        """
        日志级别调整为 DEBUG , 提示符更改为 #

         -i 将日志级别调整为INFO ,提示符更改为 >
        """
        if single_short_opts_exits(argv, 'i'):
            li_log.set_format()
            self.prompt = '> '
        else:
            li_log.set_format(logging.DEBUG)
            self.prompt = '# '

    @staticmethod
    def do_env(argv):
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

    @staticmethod
    def do_exit(argv):
        """exit the program."""
        print("bye.")
        exit(0)

    def do_history(self, argv):
        """ 查看命令历史，命令被记录为日志的形式，实际上是调用 vi 查看日志"""
        log = deep_get(self.__config, ['sip', 'log']) or 'sip.log'

        run('vi {}'.format(log))

    @staticmethod
    def do_pwd(argv):
        """
        脚本的根目录，即该脚本的绝对路径 去除sip/sip.py后
        """
        print(os.getcwd())

    @staticmethod
    def do_pull(argv):
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

    @run_on_uat
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

    def complete_backup(self, text, line, begin_idx, end_idx):

        input_apps = line.split()
        if '-a' in input_apps:
            return None

        backup_origin = deep_get(self.__config, ['backup', 'origin'])
        origin_apps = list(map(lambda war: war.replace('.war', ''),
                               [war for war in os.listdir(backup_origin) if war.endswith('.war')]))

        un_input_apps = [war for war in origin_apps if war not in input_apps]
        un_input_apps.append('-a')
        return complete_keys(line, un_input_apps, text)

    def complete_config(self, text, line, begin_idx, end_idx):

        keys = line.split()
        del keys[0]

        # 当最后一位为待补全时，剔除
        if text:
            keys.pop()
        # 去掉 config
        keys.reverse()

        d = self.__config
        #

        d = deep_get(d, keys, reverse=False)
        # while keys:
        #     key = keys.pop()
        #     d = d.get(key, {})
        #
        #     if not isinstance(d, dict):
        #         break

        if isinstance(d, dict):
            return list(map(lambda x: x + " ", [k for k in d.keys() if k.startswith(text)]))

    @staticmethod
    def complete_debug(text, line, begin_idx, end_idx):

        return complete_keys(line, ('-i',), text)

    @staticmethod
    def complete_env(text, line, begin_idx, end_idx):

        return complete_keys(line, os.environ.keys(), text)


def main():
    os.chdir(re.sub(r'sip/sip.py$', '', __file__))
    li_decorator.env = os.environ.get(SIP_ENV, '')

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


if __name__ == '__main__':
    main()
