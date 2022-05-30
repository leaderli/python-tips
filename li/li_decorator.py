import functools

env = 'uat'


def run_on_uat(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        assert env == 'uat', 'function only support run on uat , now is ' + env
        return func(*args, **kwargs)

    return wrapper
