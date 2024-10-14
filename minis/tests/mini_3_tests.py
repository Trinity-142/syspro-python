from solutions.mini_3 import solution
import pytest


@pytest.mark.parametrize("input, expected", [("1 2 | 3 4", [[1, 2], [3, 4]]),
                                             ("1 2 3 | 4 5 6", [[1, 2, 3], [4, 5, 6]]),
                                             ("1 | 2", [[1], [2]]),
                                             ("-1.5 5.75 3 | 3.43 10.213 -30", [[-1.5, 5.75, 3], [3.43, 10.213, -30]])])
def test(input, expected):
    assert solution(input) == expected
