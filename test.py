import functools

one = set()
print(type(one) )


def reg(func):
    one.add(func.__name__)

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


@reg
def hello(a: int):
    pass


print('hello' in one)
print('hello1' in one)
