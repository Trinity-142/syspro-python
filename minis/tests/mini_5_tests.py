from minis.solutions.mini_5 import specialize, sum


def test():
    y_const = specialize(sum, y=1)
    assert y_const(10) == 11

    const_y_sep = specialize(sum, 1)
    assert const_y_sep(y=10) == 11

    const_y = specialize(sum, 1, y=10)
    assert const_y() == 11

    x_const = specialize(sum, x=1)
    assert x_const(y=10) == 11

    const_x_sep = specialize(sum, 1)
    assert const_x_sep(y=10) == 11

    x_y = specialize(sum, x=1, y=5)
    assert x_y() == 6

    x_y_sep = specialize(sum, x=1)
    assert x_y_sep(y=5) == 6

    y_x = specialize(sum, y=1, x=5)
    assert y_x() == 6

    y_x_sep = specialize(sum, y=1)
    assert y_x_sep(x=5) == 6

test()
