from li.li_bash import run
from li.li_cmd import LiCmd


class Git(LiCmd):

    def do_update(self, args):
        print('------------------------')
        print(run('git rev-parse --short HEAD'))
        print('------------------------')
        print(run('echo 123'))
        print('------------------------')
        print(run('echo123'))
        print('------------------------')
