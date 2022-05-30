import subprocess
from subprocess import Popen

from li.li_cmd import LiCmd


class Git(LiCmd):

    def do_update(self, args):
        with Popen('git rev-parse --short HEAD', shell=True, stdout=subprocess.PIPE) as sha:
            print('sha:', sha.stdout.read())
        pass
