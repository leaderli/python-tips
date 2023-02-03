import logging

logging.basicConfig(format='%(levelname)s:%(message)s')


# logging.basicConfig(format='%(message)s')


def get_logger(name, file):
    # create logger for prd_ci
    log = logging.getLogger(name)
    log.setLevel(level=logging.INFO)

    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s  %(message)s')

    # create file handler for logger.
    fh = logging.FileHandler(file)
    fh.setLevel(level=logging.DEBUG)
    fh.setFormatter(formatter)

    # add handlers to logger.
    log.addHandler(fh)
    log.propagate = False
    return log


def set_format(level=logging.INFO):
    logging.root.setLevel(level)
    logging.debug('test')
    logging.info('test')


def format_table(big_arr):
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
                return template.format(*expand)
            else:
                return arr

        return

    return big_arr
