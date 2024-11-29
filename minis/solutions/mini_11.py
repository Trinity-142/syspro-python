def cycle(iterable):
    while iterable:
        for elem in iterable:
            yield elem


def chain(*args):
    for iterable in args:
        for elem in iterable:
            yield elem


def take(seq, n):
    res = []
    for i in range(n):
        try:
            res.append(next(seq))
        except StopIteration:
            break
    return res
