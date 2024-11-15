import functools


def deprecated(func=None, since="", will_be_removed=""):
    if func is None:
        return functools.partial(deprecated, since=since, will_be_removed=will_be_removed)

    @functools.wraps(func)
    def inner(*args, **kwargs):
        since_str = f" since version {since}" if since != "" else ""
        removed_str = f"version {will_be_removed}" if will_be_removed != "" else "future versions"
        print(f"Warning: function {func.__name__} is deprecated{since_str}. It will be removed in {removed_str}.")
        return func(*args, **kwargs)

    return inner


@deprecated(since="4.0", will_be_removed="5.0")
def since_and_will():
    print("from since till will")


@deprecated(since="4.0")
def since():
    print("from since till ...")


@deprecated(will_be_removed="5.0")
def will():
    print("from ... till will")


@deprecated
def without():
    print("from ... till ...")


@deprecated(will_be_removed="5.0")
def with_params(x, y):
    print(f"{x} + {y} = {x + y}")


since_and_will()
since()
will()
without()
with_params(5, 3)
