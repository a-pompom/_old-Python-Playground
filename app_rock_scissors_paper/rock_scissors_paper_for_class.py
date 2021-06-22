import random


class Hand:
    """ じゃんけんの手の表現を責務に持つ"""

    # 手の候補
    hands = ['rock', 'scissors', 'paper']
    # 手と対応する数値を管理 勝敗判定で利用
    hand_numbers = {'rock': 0, 'paper': 1, 'scissors': 2, 'tail': 3}

    def __init__(self, hand_input='', is_random_generate=False):
        """
        イニシャライザ

        :param hand_input: 入力値 じゃんけんの手の候補
        :param is_random_generate: 手をランダム生成するか
        """
        if is_random_generate:
            self.hand = self._generate_random_hand()
            return

        self._hand_input = hand_input
        self.hand = ''

    def _generate_random_hand(self):
        """
        じゃんけんの手を生成

        :return: じゃんけんの手
        """
        generated_hand_number = random.randint(0, len(self.hands) - 1)

        return self.hands[generated_hand_number]

    def is_valid(self):
        if self._hand_input in self.hands:
            self.hand = self._hand_input
            return True

        return False


class RockScissorsPaperGame:
    """ じゃんけんゲームの制御を責務に持つ """

    def __init__(self):
        pass

    def start(self):
        """
        じゃんけんゲームループを開始

        """
        while True:
            hand_input = input('じゃんけんの手を入力してください(ENDで終了)。')

            # 終了
            if hand_input == 'END':
                return

            user_hand = Hand(hand_input)
            # バリデーション
            if not user_hand.is_valid():
                print('rock, scissors, paperのいずれかを入力してください。')
                continue

            # 勝敗判定
            cpu_hand = Hand(is_random_generate=True)
            self.judge(user_hand, cpu_hand)

    def judge(self, user: Hand, cpu: Hand):
        """
        じゃんけんの勝敗判定

        :param user: ユーザの手
        :param cpu: 相手の手
        """
        # あいこ
        if user.hand == cpu.hand:
            print('DRAW')
            return

        # 勝ち
        # ユーザの手と相手の手を数値化したときの差が「1」であるとき、ユーザの勝利 先頭はそのままでは直前と比較できないのでローテーション
        is_user_win = Hand.hand_numbers[user.hand] - Hand.hand_numbers[cpu.hand] == 1
        if user == 'rock':
            is_user_win = Hand.hand_numbers['tail'] - Hand.hand_numbers[cpu.hand] == 1

        if is_user_win:
            print('YOU WIN!!')
            return

        # 負け
        print('YOU LOSE...')


def main():
    game = RockScissorsPaperGame()
    game.start()


if __name__ == '__main__':
    main()
