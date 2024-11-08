def sum(x, y):
    return x + y


def specialize(func, *args1, **kwargs1):
    def ret(*args2, **kwargs2):
        args = args1 + args2
        kwargs = {**kwargs1, **kwargs2}
        return func(*args, **kwargs)
    return ret
