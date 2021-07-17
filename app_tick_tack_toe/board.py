import dataclasses

from string_builder import StringBuilder
from coordinate import Coordinate

# 盤面のマスの初期値
INITIAL_BOARD_MARK = '!'


@dataclasses.dataclass
class BoardStatus:
    """ 盤面の状態管理を責務に持つ """
    coordinate: dict[tuple[int, int], str]
    size: int

    def __post_init__(self):
        self.coordinate = {(x, y): INITIAL_BOARD_MARK
                           for x in range(0, self.size)
                           for y in range(0, self.size)}


class BoardView:
    """ 盤面の表示部分を責務に持つ """

    # マスの間の区切り線
    BORDER_LINE = '---- ---- ----'

    def __init__(self, status: BoardStatus):
        self.status = status

    def __str__(self):
        return self._generate_view()

    def _generate_view(self) -> str:
        """
        盤面文字列の生成 具体的な文字列はドキュメント参照

        :return: 文字列化した盤面
        """
        builder = StringBuilder()

        # 横列を1行ずつ構築
        for y in range(0, self.status.size):
            builder.append_line(self._generate_mark_line(y))

            # 末尾行は改行を含むと不自然な空白行が出力されてしまうので、改行なしとする
            is_tail = y == self.status.size - 1
            builder.append(self.BORDER_LINE) if is_tail else builder.append_line(self.BORDER_LINE)

        return builder.text

    def _generate_mark_line(self, line_number: int):
        """
        マスの行を生成

        :param line_number: 行番号 対応するマスの値を取得するために利用
        :return: マスの値や空白を描画した行文字列
        """
        builder = StringBuilder()
        # 描画のバランスを考慮すると、空白は一律同一ではなく、間隔を変えた方が見映えがいい
        # よって、位置ごとの空白を保持しておく
        space = {'head': '  ', 'mid': '    ', 'tail': ''}
        marks = [self.status.coordinate[line_number, x] for x in range(0, self.status.size)]

        # 「  !    !    !」のようにマークを印字
        for i in range(0, self.status.size):
            # 先頭
            if i == 0:
                builder.append(f'{space["head"]}{marks[i]}')
                continue
            # 末尾
            if i == self.status.size - 1:
                builder.append(f'{space["mid"]}{marks[i]}{space["tail"]}')
                continue
            # 中間
            builder.append(f'{space["mid"]}{marks[i]}')

        return builder.text


class Board:
    """ 盤面を表示する要素の保持を責務に持つ"""

    def __init__(self, size=3):
        self.status = BoardStatus(size=size, coordinate={})
        self.view = BoardView(self.status)

    @property
    def size(self):
        return self.status.size

    def update(self, coordinate: Coordinate):
        """
        盤面を座標で更新

        :param coordinate: 更新対象の座標
        """

        self.status.coordinate[(coordinate.x, coordinate.y)] = coordinate.value
