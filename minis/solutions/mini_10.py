import functools


class Singleton:
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls, *args, **kwargs)
        return cls.instance


def singleton(cls):
    orig_new = cls.__new__
    instance = None

    @functools.wraps(orig_new)
    def __new__(cls, *args, **kwargs):
        nonlocal instance
        if instance is None:
            instance = orig_new(cls, *args, **kwargs)
        return instance

    cls.__new__ = __new__
    return cls


@singleton
class DecoratedCounter:
    pass


class Counter:
    pass


class MixinCounter(Singleton, Counter):
    pass


if __name__ == '__main__':
    mc1 = MixinCounter()
    mc2 = MixinCounter()
    assert id(mc1) == id(mc2)

    dc1 = DecoratedCounter()
    dc2 = DecoratedCounter()
    assert id(dc1) == id(dc2)
