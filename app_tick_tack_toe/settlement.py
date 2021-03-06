from app_tick_tack_toe.board import BoardStatus, INITIAL_BOARD_MARK
from app_tick_tack_toe.exception import GameSettled


class Settlement:
    """ 勝敗判定を責務に持つ """

    MESSAGE_DRAW = '引き分けです。'
    MESSAGE_SETTLED_1P = 'プレイヤー1の勝ちです。'
    MESSAGE_SETTLED_2P = 'プレイヤー2の勝ちです。'

    def __init__(self, status: BoardStatus):
        self.status = status

    def inspect(self):
        """
        勝敗を判定

        """

        self._inspect_vertical()
        self._inspect_horizontal()
        self._inspect_diagonal()

        self._inspect_all_filled()

    def _inspect_all_filled(self):
        """
        全ての盤面が埋められたか判定

        """

        for x in range(0, self.status.size):
            for y in range(0, self.status.size):

                if self.status.coordinate[(x, y)] == INITIAL_BOARD_MARK:
                    return

        raise GameSettled(self.MESSAGE_DRAW)

    def _is_same_mark(self, x: int, y: int) -> bool:
        """
        判定対象座標のマークが現在プレイヤーのものと同一か判定

        :param x: x座標
        :param y: y座標
        :return: True-> 一致 False-> 不一致
        """

        return self.status.coordinate[(x, y)] == self.status.player.get_mark()

    def _settle_winner(self):
        """
        勝者を決定

        """

        # 1P
        if self.status.player.current == self.status.player.CANDIDATE.PLAYER_1:
            raise GameSettled(self.MESSAGE_SETTLED_1P)

        # 2P
        raise GameSettled(self.MESSAGE_SETTLED_2P)

    def _inspect_horizontal(self):
        """
        横方向の勝敗判定 横の盤が1人のプレイヤーで埋められていれば、勝敗が確定
        """

        # いずれかの行で揃っているか判定するために保持
        horizontal_same_count = 0

        for y in range(0, self.status.size):

            # 横の判定
            for x in range(0, self.status.size):
                if self._is_same_mark(x, y):
                    horizontal_same_count += 1
            # 揃ったか
            else:
                if horizontal_same_count == self.status.size:
                    self._settle_winner()
                horizontal_same_count = 0

    def _inspect_vertical(self):
        """
        縦方向の勝敗判定 縦の盤が1人のプレイヤーで埋められていれば、勝敗が確定
        """

        # いずれかの列で揃っているか判定するために保持
        vertical_same_count = 0

        for x in range(0, self.status.size):

            # 縦の判定
            for y in range(0, self.status.size):

                if self._is_same_mark(x, y):
                    vertical_same_count += 1
            # 揃ったか
            else:
                if vertical_same_count == self.status.size:
                    self._settle_winner()
                vertical_same_count = 0

    def _inspect_diagonal(self):
        """
        斜め方向の勝敗判定 斜めの盤が1人のプレイヤーで埋められていれば、勝敗が確定
        """

        # いずれかの斜め線で揃っているか判定するために保持
        diagonal_same_count = 0

        # 左斜め
        for x, y in zip(range(0, self.status.size), range(0, self.status.size)):
            if self._is_same_mark(x, y):
                diagonal_same_count += 1
        # 揃ったか
        else:
            if diagonal_same_count == self.status.size:
                self._settle_winner()
            diagonal_same_count = 0

        # 右斜め
        for x, y in zip(reversed(range(0, self.status.size)), range(0, self.status.size)):
            if self._is_same_mark(x, y):
                diagonal_same_count += 1
        # 揃ったか
        else:
            if diagonal_same_count == self.status.size:
                self._settle_winner()
