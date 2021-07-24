from typing import Optional

from app_tick_tack_toe.exception import InvalidCoordinateException


class Coordinate:
    """ 座標の保持・座標が妥当かどうかのバリデーションを責務に持つ """

    def __init__(self, value: str, max_size: Optional[int] = None):
        self.x = None
        self.y = None
        self.value = value

        if not max_size:
            from app_tick_tack_toe.board import DEFAULT_BOARD_SIZE
            max_size = DEFAULT_BOARD_SIZE - 1

        # 座標がとりうる最大値/最小値
        self._max_size = max_size
        self._min_size = 0

    def assign(self, raw_input: str):
        """
        入力値を2次元のxy座標へ割り当て

        :param raw_input: 0個以上のスペースを含む、カンマ区切りの2つの数字で構成された文字列 ex) 「1,2」, 「 0 , 4」
        """

        if not raw_input:
            raise InvalidCoordinateException()

        # 数値形式の座標へ
        x, y = self._validate_range(*self._convert(raw_input))
        self.x, self.y = x, y

    def _convert(self, raw_input: str) -> tuple[int, int]:
        """
        数字形式の座標を数値形式の座標へ変換

        :param raw_input: 入力文字列
        :return: x座標, y座標を表す数値
        """

        # 空白は座標に影響しない要素なので、必要なトークンのみとするために削除
        space_trimmed_input = raw_input.replace(' ', '').replace('　', '')
        # 数字形式の座標へ
        character_x, character_y = self._split_by_comma(space_trimmed_input)

        try:
            # 数値へ変換できるか
            x = int(character_x)
            y = int(character_y)

            return x, y
        except ValueError:
            raise InvalidCoordinateException

    def _split_by_comma(self, space_trimmed_input: str) -> tuple[str, str]:
        """
        入力の数字をカンマ区切りで分割

        :param space_trimmed_input: スペースが除外された入力値 「<数字>,<数字>」であることを期待
        :return: x座標,y座標を表す数字
        """

        separated = space_trimmed_input.split(',')
        # x,yによる座標なので、ペア以外は受け付けない
        is_pair = len(separated) == 2
        if not is_pair:
            raise InvalidCoordinateException

        return separated[0], separated[1]

    def _validate_range(self, x: int, y: int) -> tuple[int, int]:
        """
        x,y座標が最小・最大値の範囲内に収まっているか検証

        :param x: x座標
        :param y: y座標

        :return x座標, y座標を表す数値 後続の処理でバリデーション結果を利用しやすくするため、入力をそのまま返却
        """

        is_x_over_range = not self._min_size <= x <= self._max_size
        is_y_over_range = not self._min_size <= y <= self._max_size

        if is_x_over_range or is_y_over_range:
            raise InvalidCoordinateException

        return x, y
