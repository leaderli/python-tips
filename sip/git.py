from li.li_bash import bash
from li.li_cmd import LiCmd


class Git(LiCmd):

    def do_update(self, args):
        print('------------------------')
        print(bash('git rev-parse --short HEAD'))
        print('------------------------')
        print(bash('echo 123'))
        print('------------------------')
        print(bash('echo123'))
        print('------------------------')
