import functools
import logging

env = 'uat'


def run_on_uat(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        assert 'pdu' not in env, 'function only support run on uat or local, now is ' + env
        return func(*args, **kwargs)

    return wrapper


def log_args(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(*args)
        print(**kwargs)
        # logging.debug(*args, ** kwargs)
        return func(*args, **kwargs)

    return wrapper
