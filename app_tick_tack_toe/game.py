from app_tick_tack_toe.board import Board
from app_tick_tack_toe.coordinate import Coordinate
from app_tick_tack_toe.exception import AlreadyBoardFilledException, GameSettled, InvalidCoordinateException
from app_tick_tack_toe.string_builder import StringBuilder

LINE_BREAK = StringBuilder.LINE_BREAK


class StartPhase:
    """ 開始処理として、開始メッセージ・初期盤面の表示を責務に持つ """
    START_MESSAGE = 'ゲームを開始します。'

    def proceed(self, board: Board):
        """
        phase進行として、開始メッセージ・初期盤面を表示

        :param board: 盤面
        """
        print(self.START_MESSAGE)
        print(board.view)


class MainPhase:
    INPUT_PROMPT = f'手を入力してください。{LINE_BREAK}'
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
                print(board.view)
                print(settled.settle_message)
                return

            # 次のターンへ
            print(board.view)
            print('')
            board.status.player.change()

    def _read_input(self) -> str:
        """
        ユーザの入力値を受け取る

        :return: 入力文字列
        """
        return input(self.INPUT_PROMPT)


class Game:

    def __init__(self):
        self._phases = [StartPhase(), MainPhase()]

    def start(self):
        board = Board()
        [phase.proceed(board) for phase in self._phases]


if __name__ == '__main__':
    game = Game()
    game.start()
