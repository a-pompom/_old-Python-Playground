from board import Board
from coordinate import Coordinate, InvalidCoordinateException
from player import Player


class StartPhase:
    """ 開始処理として、開始メッセージ・初期盤面の表示を責務に持つ """
    START_MESSAGE = 'start'

    def proceed(self, board: Board):
        """
        phase進行として、開始メッセージ・初期盤面を表示

        :param board: 盤面
        """
        print(self.START_MESSAGE)
        print(board.view)


class MainPhase:
    INPUT_PROMPT = '手を入力してください。\n'
    END_INPUT = 'END'

    def proceed(self, board: Board):
        """
        メインのゲームループを実行

        :param board: 盤面
        """
        player = Player()

        while True:
            raw_input = self._read_input()

            # 終了判定
            if raw_input == self.END_INPUT:
                return

            # 盤面更新
            coordinate = Coordinate(player.get_mark(), board.size)
            try:
                coordinate.assign(raw_input)
            except InvalidCoordinateException as e:
                print(e.MESSAGE)
                continue

            board.update(coordinate)
            print(board.view)
            player.change()

    def _read_input(self) -> str:
        """
        ユーザの入力値を受け取る

        :return: 入力文字列
        """
        return input(self.INPUT_PROMPT)


class EndPhase:
    pass


class Game:

    def __init__(self):
        self._phases = [StartPhase(), MainPhase()]

    def start(self):
        board = Board()
        [phase.proceed(board) for phase in self._phases]


if __name__ == '__main__':
    game = Game()
    game.start()
