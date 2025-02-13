from minis.solutions.mini_4 import solution
import pytest

@pytest.mark.parametrize("input, expected", [({"Ivanov": 97832, "Petrov": 55521, "Kuznecov": 97832}, {97832: ("Ivanov", "Kuznecov"), 55521: "Petrov"}),
                                             ({"Ivanov": 97832, "Petrov": 55521, "Kuznecov": 66666}, {97832: "Ivanov", 55521: "Petrov", 66666: "Kuznecov"}),
                                             ({"Ivanov": 97832, "Petrov": 55521, "Kuznecov": 97832, "Fedorov": 97832}, {97832: ("Ivanov", "Kuznecov", "Fedorov"), 55521: "Petrov"}),
                                             ({'Ivanov': 97832, 'Petrov': 55521, 'Kuznecov': 97832}, {97832: ("Ivanov", "Kuznecov"), 55521: "Petrov"}),
                                             ({12: 3, 14: 2, 16: 1, 11: 3, 15: 2}, {3: (12, 11), 2: (14, 15), 1: 16})])
def test(input, expected):
    assert solution(input) == expected