import pytest
from typing import TypeAlias

from app_tick_tack_toe.board import BoardStatus, DEFAULT_BOARD_SIZE
from app_tick_tack_toe.player import Player
from app_tick_tack_toe.settlement import Settlement, GameSettled

from app_tick_tack_toe.tests.util import FixtureRequest, FixtureParam

BoardCoordinate: TypeAlias = dict[tuple[int, int], str]


def get_draw_param():
    """
    引き分けをつくり出すためのパラメータを生成

    :return: 座標辞書・テストIDのリストを格納したオブジェクト
    """

    draw: FixtureParam[BoardCoordinate] = FixtureParam()
    draw.append_param(
        {
            (0, 0): '○', (0, 1): '×', (0, 2): '○',
            (1, 0): '×', (1, 1): '×', (1, 2): '○',
            (2, 0): '×', (2, 1): '○', (2, 2): '×',
        }
    ).append_id('draw')

    return draw


draw_param = get_draw_param()


@pytest.fixture(params=draw_param.params, ids=draw_param.ids)
def param_draw(request: FixtureRequest[BoardCoordinate]) -> BoardCoordinate:
    return request.param


def get_settled_param():
    """
    勝利状態をつくり出すためのパラメータを生成

    :return: 座標辞書・テストIDのリストを格納したオブジェクト
    """

    settled: FixtureParam[BoardCoordinate] = FixtureParam()
    settled.append_param(
        {
            (0, 0): '○', (0, 1): '×', (0, 2): '○',
            (1, 0): '○', (1, 1): '×', (1, 2): '○',
            (2, 0): '○', (2, 1): '○', (2, 2): '×',
        }
    ).append_id('vertical').append_param(
        {
            (0, 0): '○', (0, 1): '×', (0, 2): '×',
            (1, 0): '×', (1, 1): '×', (1, 2): '○',
            (2, 0): '○', (2, 1): '○', (2, 2): '○',
        }
    ).append_id('horizontal').append_param(
        {
            (0, 0): '○', (0, 1): '×', (0, 2): '×',
            (1, 0): '×', (1, 1): '○', (1, 2): '○',
            (2, 0): '○', (2, 1): '×', (2, 2): '○',
        }
    ).append_id('left diagonal').append_param(
        {
            (0, 0): '○', (0, 1): '×', (0, 2): '○',
            (1, 0): '×', (1, 1): '○', (1, 2): '○',
            (2, 0): '○', (2, 1): '×', (2, 2): '×',
        }
    ).append_id('right diagonal')

    return settled


settled_param = get_settled_param()


@pytest.fixture(params=settled_param.params, ids=settled_param.ids)
def param_settled(request: FixtureRequest[BoardCoordinate]) -> BoardCoordinate:
    return request.param


class TestSettlement:

    def test_no_settlement(self):

        # GIVEN
        status = BoardStatus(size=DEFAULT_BOARD_SIZE, coordinate={}, player=Player())
        sut = Settlement(status)
        # WHEN
        try:
            sut.inspect()
        except GameSettled:
            assert False

    def test_draw(self, param_draw: BoardCoordinate):

        # GIVEN
        status = BoardStatus(size=DEFAULT_BOARD_SIZE, coordinate={}, player=Player())
        status.coordinate = param_draw

        sut = Settlement(status)

        # WHEN
        with pytest.raises(GameSettled) as s:
            sut.inspect()
        assert s.value.settle_message == Settlement.MESSAGE_DRAW

    def test_settled(self, param_settled):
        # GIVEN
        status = BoardStatus(size=DEFAULT_BOARD_SIZE, coordinate={}, player=Player())
        status.coordinate = param_settled

        sut = Settlement(status)

        # WHEN
        with pytest.raises(GameSettled) as s:
            sut.inspect()
        assert s.value.settle_message == Settlement.MESSAGE_SETTLED_1P or \
               s.value.settle_message == Settlement.MESSAGE_SETTLED_2P
