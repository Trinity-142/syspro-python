import functools


def coroutine(func):
    @functools.wraps(func)
    def firstnext(*args, **kwargs):
        gener = func(*args, **kwargs)
        next(gener)
        return gener

    return firstnext


@coroutine
def storage():
    values = set()
    was_there = False

    while True:
        val = yield was_there
        was_there = val in values
        if not was_there:
            values.add(val)


if __name__ == '__main__':
    st = storage()
    assert not st.send(42)
    assert st.send(42)
