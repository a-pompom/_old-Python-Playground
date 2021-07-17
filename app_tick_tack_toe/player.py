import dataclasses


@dataclasses.dataclass
class Candidate:
    """ 現在プレイヤーの候補 """
    PLAYER_1: str = 'FIRST'
    PLAYER_2: str = 'SECOND'


@dataclasses.dataclass
class Mark:
    """ 盤面へ印字する記号 """
    FIRST: str = '○'
    SECOND: str = '×'


class Player:
    """ ゲームのプレイヤーの状態管理を責務に持つ """

    CANDIDATE: Candidate = Candidate()
    MARK: Mark = Mark()

    def __init__(self):
        # 現在プレイヤー
        self.current = self.CANDIDATE.PLAYER_1

    def get_mark(self):
        """
        盤面へ印字する記号を取得

        :return: ○ or ×
        """

        return self.MARK.__getattribute__(self.current)

    def change(self):
        """
        プレイヤーを切り替え
        """

        if self.current == self.CANDIDATE.PLAYER_1:
            self.current = self.CANDIDATE.PLAYER_2
            return

        self.current = self.CANDIDATE.PLAYER_1
