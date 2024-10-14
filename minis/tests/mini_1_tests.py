from solutions.mini_1 import solution
import pytest


@pytest.mark.parametrize("input, expected", [(10, 2),
                                             (647, 5),
                                             (-123, 3),
                                             (-1, 2),
                                             (-5, 3),
                                             (-345, 6)])
def test(input, expected):
    assert solution(input) == expected
