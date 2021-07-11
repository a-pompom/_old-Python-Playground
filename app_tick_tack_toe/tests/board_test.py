import pytest

from .expected.board import get_initial_board
from ..board import Board


def test_initial_board(capfd: pytest.CaptureFixture):
    # GIVEN
    expected = get_initial_board()
    # WHEN
    sut = Board()
    print(sut.view)
    actual = capfd.readouterr().out
    # THEN
    assert actual == expected
