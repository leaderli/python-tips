import os
from cmd import Cmd


class Sip(Cmd):

    def cmdloop(self, intro=None):
        print(self.intro)

        while True:
            try:
                super().cmdloop(intro="")
                break
            except KeyboardInterrupt:
                print("^C")

    def do_env(self, key):
        """ get environment variable , default get 'com_pccc_sip_env' """
        if not key:
            key = 'com_pccc_sip_env'
        return os.environ.get(key)

    def complete_hello(self, text, line, begidx, endidx):
        return ['stranger']

    def help_hello(self):
        """Says hello. If you provide a name, it will greet you with it."""
        print('help_hello', self.help_hello.__doc__)

    def do_hello(self, args):
        """Says hello. If you provide a name, it will greet you with it."""
        if len(args) == 0:
            name = 'stranger'
        else:
            name = args
        print("Hello, %s" % name)

    def do_exit(self, args):
        """exit the program."""
        print("bye.")
        exit(0)


if __name__ == '__main__':
    sip = Sip()
    # print(dir(prompt))
    # for func in [func for func in dir(prompt) if
    #              callable(getattr(prompt, func)) and func.startswith("do_") and func not in ['do_help']]:
    #     print(func)
    #     getattr(prompt, func)(sys.argv[1:])

    sip.prompt = '> '
    sip.cmdloop('...')
