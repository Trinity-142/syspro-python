import functools

def singleton(cls):
    orig_new = cls.__new__
    orig_init = cls.__init__
    instance = None
    initialized = False

    @functools.wraps(orig_new)
    def __new__(cls, *args, **kwargs):
        nonlocal instance
        nonlocal initialized
        if instance is None:
            instance = orig_new(cls)
            orig_init(instance, *args, **kwargs)
            initialized = True
        return instance
    cls.__new__ = __new__

    @functools.wraps(orig_init)
    def __init__(self, *args, **kwargs):
        nonlocal initialized
        if not initialized:
            orig_init(self, *args, **kwargs)
            initialized = True
    cls.__init__ = __init__

    return cls


@singleton
class DecoratedCounter:

    def __init__(self, x):
        self.x = x
        print("Hi")
    pass

if __name__ == '__main__':
    dc1 = DecoratedCounter(1)
    dc2 = DecoratedCounter(2)
    dc2 = DecoratedCounter(3)
    assert id(dc1) == id(dc2)

