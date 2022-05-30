class Log(object):

    def __init__(self, _func=None, *, name='default'):
        self.name = name
        self._func = _func

    def __call__(self, *_args, **_kwargs):
        def wrapper(*args, **kwargs):
            print('before ' + self.name)
            return _args[0](*args, **kwargs)

        # if self._func:
        #     return self._func
        if not callable(self._func):
            return wrapper

        print('-- before not parameter -- ')
        return self._func(*_args, **_kwargs)


@Log
def hello(name):
    return 'hello ' + name


@Log(name='li')
def hello2(name):
    return 'hello ' + name


print(hello('one'))
print(hello2('two'))
