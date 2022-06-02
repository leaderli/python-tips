import logging
from cmd import Cmd

log = logging.root


class LiCmd(Cmd):

    def __log__(self, _log):
        global log
        log = _log

    def cmdloop(self, intro='created by leaderli'):

        try:
            super().cmdloop(intro=intro)
        except KeyboardInterrupt:
            exit()

    def postcmd(self, stop, line):

        global log
        log.info(line)

    def default(self, line):

        print("unknown {} command: {}".format(self.__class__.__name__, line))
        # noinspection PyTypeChecker
        super().do_help(None)

    def emptyline(self):
        pass
