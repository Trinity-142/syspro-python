from solutions.mini_2 import solution
import pytest


@pytest.mark.parametrize("input, expected", [("[1, 2, 3], [\"a\", \"b\"]", [(1, "a"), (2, "b")]),
                                             ("[1, 2, 3], [\"a\", \"b\", \"c\"]", [(1, "a"), (2, "b"), (3, "c")]),
                                             ("[1, 2], [\"a\", \"b\", \"c\"]", [(1, "a"), (2, "b")]),
                                             ("[1, 2, 3], [\"one\", \"two\", \"three\"]",
                                              [(1, "one"), (2, "two"), (3, "three")]),
                                             ("[1, 2, 3], ['one', 'two']", [(1, "one"), (2, "two")])])
def test(input, expected):
    assert solution(input) == expected
