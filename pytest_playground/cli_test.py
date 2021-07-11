import pytest


def test_print(capfd: pytest.CaptureFixture):
    """
    print文の履歴を検証

    :param capfd: 標準入出力を捕捉するためのFixture
    """

    print('hello')
    print('world')
    captured = capfd.readouterr()
    assert captured.out == 'hello\nworld\n'
