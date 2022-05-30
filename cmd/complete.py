import cmd


class MyCmd(cmd.Cmd):
    def do_command(self, line):
        'do_command: [parametre[1,2]=xxx]'
        print(line)

    def complete_command(self, text, line, begidx, endidx):
        return [i
                for i in ('parametre1=', 'parametre2=')
                if i.startswith(text)]

    def do_EOF(self, line):
        'exit the program. Use  Ctrl-D (Ctrl-Z in Windows) as a shortcut'
        return True


if __name__ == "__main__":
    myCmd = MyCmd()
    myCmd.cmdloop("command 123")
