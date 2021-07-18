from board import Board
from coordinate import Coordinate, InvalidCoordinateException
from exception import AlreadyBoardFilledException
from settlement import GameSettled


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

        while True:
            raw_input = self._read_input()

            # 終了判定
            if raw_input == self.END_INPUT:
                return

            # 盤面更新
            coordinate = Coordinate(board.status.player.get_mark(), board.size)
            try:
                coordinate.assign(raw_input)
                board.update(coordinate)
            except (InvalidCoordinateException, AlreadyBoardFilledException) as e:
                print(e.MESSAGE)
                continue

            # 勝敗判定
            try:
                board.inspect_settlement()
            except GameSettled as settled:
                print(settled.message)
                return

            # 次のターンへ
            print(board.view)
            board.status.player.change()

    def _read_input(self) -> str:
        """
        ユーザの入力値を受け取る

        :return: 入力文字列
        """
        return input(self.INPUT_PROMPT)


class EndPhase:
    """ 終了メッセージの表示を責務に持つ """
    END_MESSAGE = 'ゲームを終了します。'

    def proceed(self, board: Board):
        """
        phase進行として、終了メッセージを表示

        :param board: 盤面
        """

        print(self.END_MESSAGE)


class Game:

    def __init__(self):
        self._phases = [StartPhase(), MainPhase()]

    def start(self):
        board = Board()
        [phase.proceed(board) for phase in self._phases]


if __name__ == '__main__':
    game = Game()
    game.start()
