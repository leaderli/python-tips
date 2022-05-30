from cmd import Cmd


class LiCmd(Cmd):

    def cmdloop(self, intro=None):

        try:
            super().cmdloop(intro="")
        except KeyboardInterrupt:
            exit()

    def default(self, line: str):

        print("unknown {} command: {}".format(self.__class__.__name__, line))
        # noinspection PyTypeChecker
        super().do_help(None)

    def emptyline(self):
        pass
