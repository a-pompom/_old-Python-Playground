import dataclasses
import pytest
from pytest import FixtureRequest as __FixtureRequest
from pytest_mock import MockerFixture

from app_tick_tack_toe.game import MainPhase
from app_tick_tack_toe.board import Board
from app_tick_tack_toe.coordinate import InvalidCoordinateException
from app_tick_tack_toe.settlement import Settlement
from app_tick_tack_toe.string_builder import StringBuilder

from app_tick_tack_toe.tests.expected.board import get_single_1p_board, get_single_both_player_board, \
    get_multiple_both_player_board, get_draw_board, get_1p_settled_board, get_2p_settled_board


LINE_BREAK = StringBuilder.LINE_BREAK


@dataclasses.dataclass
class GameParam:
    """ ゲームループのパラメータ管理を責務に持つ"""

    expected: str
    side_effects: list[str]


class FixtureRequest(__FixtureRequest):
    param: GameParam


class GameFixtureParam:
    """ パラメータフィクスチャの生成を責務に持つ """

    def __init__(self):
        self.params, self.ids = self._generate_params()

    def _generate_params(self) -> tuple[list[GameParam], list[str]]:
        """
        Fixtureで扱うパラメータを生成

        :return: fixtureのパラメータ, IDのリスト
        """

        params_include_ids = [

            [GameParam(
                expected=f'{InvalidCoordinateException.MESSAGE}{LINE_BREAK}',
                side_effects=['invalid', MainPhase.END_INPUT],
            ), 'invalid coordinate'],

            [GameParam(
                expected=get_single_1p_board(),
                side_effects=['0,0', MainPhase.END_INPUT],
            ), 'single 1p input'],

            [GameParam(
                expected=get_single_both_player_board(),
                side_effects=['0,0', '1,1', MainPhase.END_INPUT],
            ), 'single both player input'],
            [GameParam(
                expected=get_multiple_both_player_board(),
                side_effects=['0,0', '2,0', '1,1', '2,1', '0,2', MainPhase.END_INPUT],
            ), 'multiple both player input'],
            [GameParam(
                expected=f'{get_draw_board()}{Settlement.MESSAGE_DRAW}{LINE_BREAK}',
                side_effects=['0,0', '0,1', '1,0', '1,1', '2,1', '2,0', '0,2', '1,2', '2,2', MainPhase.END_INPUT],
            ), 'draw input'],
            [GameParam(
                expected=f'{get_1p_settled_board()}{Settlement.MESSAGE_SETTLED_1P}{LINE_BREAK}',
                side_effects=['0,0', '0,1', '1,0', '1,2', '2,0', MainPhase.END_INPUT],
            ), '1p settled'],
            [GameParam(
                expected=f'{get_2p_settled_board()}{Settlement.MESSAGE_SETTLED_2P}{LINE_BREAK}',
                side_effects=['0,0', '2,0', '0,1', '2,1', '1,0', '2,2', MainPhase.END_INPUT],
            ), '2p settled'],
        ]

        params_and_ids = tuple(zip(*params_include_ids))
        return params_and_ids[0], params_and_ids[1]


game_fixture_param = GameFixtureParam()


@pytest.fixture(params=game_fixture_param.params, ids=game_fixture_param.ids)
def param(request: FixtureRequest) -> GameParam:
    return request.param


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

    def test_proceed(self, param: GameParam, capfd: pytest.CaptureFixture, mocker: MockerFixture):
        # GIVEN
        board = Board()
        self._create_user_input_mock(param.side_effects, mocker)

        # WHEN
        sut = MainPhase()
        sut.proceed(board)

        # THEN
        actual = capfd.readouterr().out
        assert actual == param.expected
