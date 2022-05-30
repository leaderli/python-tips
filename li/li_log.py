import getopt
import logging
from typing import Union


def __basic_config__(level):
    logging.basicConfig(level=level, format='%(levelname)s:%(message)s')


def set_log(argv):
    short_opts = "d"
    long_opts = ["debug"]

    opts, args = getopt.getopt(argv, short_opts, long_opts)

    for opt, param in opts:
        if opt in ('-d', '--debug'):
            __basic_config__(logging.DEBUG)


def print_table(big_arr: Union[list, tuple]):
    """
        print table like data with fixed width
    """
    if (isinstance(big_arr, (list, tuple))) and len(big_arr) > 0 and isinstance(big_arr[0], (list, tuple)):

        fixed_widths = [0, ] * len(big_arr[0])

        for arr in [_ for _ in big_arr if isinstance(_, (tuple, list))]:

            #  use longest arr as fixed_widths arr
            if len(arr) > len(fixed_widths):
                fixed_widths = fixed_widths + [1, ] * (len(arr) - len(fixed_widths))

            for idx, x in enumerate(arr):
                if len(x) > fixed_widths[idx]:
                    fixed_widths[idx] = len(x)

        template = " ".join(('{:<%d}',) * len(fixed_widths)) % tuple(fixed_widths)

        for arr in big_arr:
            if isinstance(arr, (list, tuple)):

                # expand the arr to fixed_widths size to prevent out of range error
                expand = tuple(arr) + ('',) * (len(fixed_widths) - len(arr))
                print(template.format(*expand))
            else:
                print(arr)

        return

    print(big_arr)
