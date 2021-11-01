from math_series import __version__
from math_series.series import fibonacci
from math_series.series import lucas
from math_series.series import sum_series



def test_version():
    assert __version__ == '0.1.0'

def test_fibonacci_4():
    expected=3
    actual=fibonacci(4)
    assert actual == expected

def test_lucas_5():
    expected = 11
    actual = lucas(5)
    assert actual == expected


def test_sum_series_7():
    numb = 7
    expected = 29
    actual = sum_series(2,1,numb)
    assert actual == expected
    
