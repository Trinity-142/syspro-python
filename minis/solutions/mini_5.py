def sum(x, y):
    return x + y


def specialize(func, *args1, **kwargs1):
    def ret(*args2, **kwargs2):
        args = args1 + args2
        kwargs = {**kwargs1, **kwargs2}
        if "x" in kwargs.keys() and "y" not in kwargs.keys():
            kwargs["y"] = kwargs["x"]
            kwargs.pop("x")
        return func(*args, **kwargs)

    return ret
