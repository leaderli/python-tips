from cmd import Cmd

import li.li_decorator


class MyPrompt(Cmd):

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

    def do_quit(self, args):
        """Quits the program."""
        print("Quitting.")
        raise SystemExit


if __name__ == '__main__':
    prompt = MyPrompt()
    # print(dir(prompt))
    # for func in [func for func in dir(prompt) if
    #              callable(getattr(prompt, func)) and func.startswith("do_") and func not in ['do_help']]:
    #     print(func)
    #     getattr(prompt, func)(sys.argv[1:])

    prompt.prompt = '> '
    prompt.cmdloop('Starting prompt...')

