import pytest

from app_tick_tack_toe.tests.expected.board import get_initial_board
from app_tick_tack_toe.board import Board
from app_tick_tack_toe.coordinate import Coordinate
from app_tick_tack_toe.exception import AlreadyBoardFilledException


class TestBoard:

    def test_initial_board(self, capfd: pytest.CaptureFixture):

        # GIVEN
        expected = get_initial_board()

        # WHEN
        sut = Board()
        print(sut.view)
        actual = capfd.readouterr().out

        # THEN
        assert actual == expected

    def test_already_updated(self):

        # GIVEN
        coordinate_1p = Coordinate('○')
        coordinate_1p.assign('0,0')
        coordinate_2p = Coordinate('×')
        coordinate_2p.assign('0,0')

        # WHEN
        sut = Board()

        # THEN
        sut.update(coordinate_1p)
        with pytest.raises(AlreadyBoardFilledException):
            sut.update(coordinate_2p)
