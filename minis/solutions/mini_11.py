def cycle(iterable):
    arr = []
    for elem in iterable:
        yield elem
        arr.append(elem)
    while arr:
        for elem in arr:
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

if __name__ == '__main__':
    print(take(cycle(chain([1, 2, 3], ["a", "b"])), 9))