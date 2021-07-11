import pytest
from pytest_mock import MockerFixture

from .expected.board import get_initial_board
from ..game import StartPhase, MainPhase
from ..board import Board
from ..coordinate import InvalidCoordinateException


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


class TestMainPhase:

    def _create_user_input_mock(self, side_effects: list[str], mocker: MockerFixture):
        """
        ユーザ入力のモックを生成

        :param side_effects: ユーザ入力値のリスト
        :param mocker: MockerFixture
        """

        input_mock = mocker.Mock()
        input_mock.side_effect = side_effects
        mocker.patch.object(MainPhase, '_read_input', input_mock)

    def test_print_invalid_coordinate(self, capfd: pytest.CaptureFixture, mocker: MockerFixture):
        # GIVEN
        board = Board()
        expected = f'{InvalidCoordinateException.MESSAGE}\n'

        self._create_user_input_mock(['invalid', MainPhase.END_INPUT], mocker)

        # WHEN
        sut = MainPhase()
        sut.proceed(board)

        # THEN
        actual = capfd.readouterr().out
        assert actual == expected

    def test_update_coordinate(self, mocker: MockerFixture):
        # GIVEN
        board = Board()
        expected = '○'

        self._create_user_input_mock(['0,0', MainPhase.END_INPUT], mocker)

        # WHEN
        sut = MainPhase()
        sut.proceed(board)

        actual = board.coordinate[(0, 0)]

        # THEN
        assert actual == expected
