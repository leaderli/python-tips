import getopt


def single_short_opts_exits(args, short):
    assert len(short) == 1, 'only support single character'

    if type(args) == str:
        args = args.split()
    opts = getopt.getopt(args, short, [])[0]

    if opts:
        return opts[0][0]

    return None


def single_short_opts_param(args, short):
    assert len(short) == 1, 'only support single character'

    if type(args) == str:
        args = args.split()
    opts = getopt.getopt(args, short + ":", [])[0]
    if opts:
        return opts[0][1]

    return None
