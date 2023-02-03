import functools

env = 'uat'


def run_on_uat(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        assert 'pdu' not in env, 'function only support run on uat or local, now is ' + env
        return func(*args, **kwargs)

    return wrapper
