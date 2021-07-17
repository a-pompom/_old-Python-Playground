class Player:
    """ ゲームのプレイヤーの状態管理を責務に持つ """

    # 現在プレイヤーの候補
    CANDIDATE = {
        'player1': '1p',
        'player2': '2p'
    }

    # 盤面へ印字する記号
    MARK = {
        '1p': '○',
        '2p': '×'
    }

    def __init__(self):
        # 現在プレイヤー
        self.current = self.CANDIDATE['player1']

    def get_mark(self):
        """
        盤面へ印字する記号を取得

        :return: ○ or ×
        """

        return self.MARK[self.current]

    def change(self):
        """
        プレイヤーを切り替え
        """

        if self.current == self.CANDIDATE['player1']:
            self.current = self.CANDIDATE['player2']
            return

        self.current = self.CANDIDATE['player1']
