import pytest
from matrixpow import matrix_pow


@pytest.mark.parametrize("matrix, poww, expected", [([[4, 2],
                                                     [5, 2]], 5,
                                                    [[6544, 3032],
                                                     [7580, 3512]]),

                                                   ([[5.5, 3.3, 0],
                                                     [0, 2, 0],
                                                     [0, 0, 4.5]], 4,
                                                    [[915.0625, 847.6875, 0.0],
                                                     [0.0, 16.0, 0.0],
                                                     [0.0, 0.0, 410.0625]])])
def test(matrix, poww, expected):
    assert matrix_pow(matrix, poww) == expected
