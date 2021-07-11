from string_builder import StringBuilder
from coordinate import Coordinate


class Board:
    """ 盤面を表示する要素の保持を責務に持つ"""

    # 盤面のマスの初期値
    INITIAL_MARK = '!'
    # マスの間の区切り線
    BORDER_LINE = '---- ---- ----'

    def __init__(self, size=3):
        self.size = size
        # マスの初期化
        self.coordinate = {(x, y): self.INITIAL_MARK
                           for x in range(0, self.size)
                           for y in range(0, self.size)}

        self.view = self._generate_view()

    def update(self, coordinate: Coordinate):
        """
        盤面を座標で更新

        :param coordinate: 更新対象の座標
        """

        self.coordinate[(coordinate.x, coordinate.y)] = coordinate.value
        self.view = self._generate_view()

    def _generate_view(self) -> str:
        """
        盤面文字列の生成

        :return: 文字列化した盤面
        """
        builder = StringBuilder()
        for y in range(0, self.size):
            builder.append_line(self._generate_mark_line(y))

            # 末尾行は改行を含むと不自然な空白行が出力されてしまうので、改行なしとする
            is_tail = y == self.size - 1
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
        marks = [self.coordinate[line_number, x] for x in range(0, self.size)]

        for i in range(0, self.size):
            # 先頭
            if i == 0:
                builder.append(f'{space["head"]}{marks[i]}')
                continue
            # 中間
            if i == self.size - 1:
                builder.append(f'{space["mid"]}{marks[i]}{space["tail"]}')
                continue
            # 末尾
            builder.append(f'{space["mid"]}{marks[i]}')

        return builder.text
