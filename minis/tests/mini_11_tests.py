from minis.solutions.mini_11 import chain, take, cycle
import pytest


@pytest.mark.parametrize("iter, count, expected", [([1, 2, 3], 10, [1, 2, 3, 1, 2, 3, 1, 2, 3, 1]),
                                                   (('a', 'b', 'c'), 7, ['a', 'b', 'c', 'a', 'b', 'c', 'a']),
                                                   ([], 10, [])])
def test_cycle(iter, count, expected):
    assert take(cycle(iter), count) == expected


@pytest.mark.parametrize("iters, expected", [(([1, 2, 3], ['a', 'b'], [5, 6]), [1, 2, 3, 'a', 'b', 5, 6]),
                                             (((1, 2, 3), ["qweqwe", 'fff'], []), [1, 2, 3, "qweqwe", 'fff'])])
def test_chain(iters, expected):
    assert list(chain(*iters)) == expected
