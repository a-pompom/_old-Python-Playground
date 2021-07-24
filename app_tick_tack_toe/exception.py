class InvalidCoordinateException(Exception):
    """ 不正な座標 """
    MESSAGE = '座標の入力として正しくありません。'


class AlreadyBoardFilledException(Exception):
    """ 盤面座標入力済 """

    MESSAGE = '既に入力済みです。'


class GameSettled(Exception):
    """ ゲーム決着の表現を責務に持つ """

    def __init__(self, message: str):
        self.settle_message = message
        super().__init__()

