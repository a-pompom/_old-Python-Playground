import pytest

from app_tick_tack_toe.tests.expected.board import get_initial_board
from app_tick_tack_toe.game import StartPhase
from app_tick_tack_toe.board import Board


class TestStartPhase:

    def test_init(self, capfd: pytest.CaptureFixture):
        # GIVEN
        expected_board = get_initial_board()
        expected = f'{StartPhase.START_MESSAGE}\n{expected_board}'
        board = Board()

        # WHEN
        sut = StartPhase()
        sut.proceed(board)

        actual = capfd.readouterr().out
        # THEN
        assert actual == expected
