import getopt


def short_opts_exits(args, short):
    assert len(short) == 1, 'only support single character'

    if type(args) == str:
        args = args.split()
    opts = getopt.getopt(args, short, [])[0]

    for opt, param in opts:
        if opt in ('-' + short):
            return opt

    return None


print(short_opts_exits('e', 'd'))
