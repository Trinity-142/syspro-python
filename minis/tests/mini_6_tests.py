from solutions.mini_6 import flatten
import pytest


@pytest.mark.parametrize("arr, depth, expected", [([1, 2, [4, 5], [6, [7]], 8], float("inf"), [1, 2, 4, 5, 6, 7, 8]),
                                                  ([1, 2, [4, 5], [6, [7]], 8], 1, [1, 2, 4, 5, 6, [7], 8]),
                                                  ([1, 2, [4, [5, [2, 4, [6, 4, [1, 3]]]]], [6, [7]], 8], 3,
                                                   [1, 2, 4, 5, 2, 4, [6, 4, [1, 3]], 6, 7, 8])])
def test(arr, depth, expected):
    assert flatten(arr, depth) == expected
