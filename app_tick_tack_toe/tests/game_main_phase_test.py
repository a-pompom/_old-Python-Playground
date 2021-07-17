import dataclasses
import pytest
from pytest_mock import MockerFixture

from .expected.board import get_single_1p_board, get_single_both_player_board, get_multiple_both_player_board
from ..game import MainPhase
from ..board import Board
from ..coordinate import InvalidCoordinateException
from pytest import FixtureRequest as __FixtureRequest


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
                expected=f'{InvalidCoordinateException.MESSAGE}\n',
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
                side_effects=['0,0', '0,2', '1,1', '1,2', '2,2', MainPhase.END_INPUT],
            ), 'multiple both player input']
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
