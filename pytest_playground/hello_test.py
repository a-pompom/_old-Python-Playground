import pytest
import sys
def say_hello():
    return 'Hello pytest'

def test_hello():
    print(sys.path)
    actual = say_hello()
    expected = 'Hello pytest'

    assert actual == expected
