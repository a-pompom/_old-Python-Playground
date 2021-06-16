import random
from typing import Union, TypeGuard, TypeAlias

Hand: TypeAlias = Union['rock', 'scissors', 'paper']

hands = ['rock', 'scissors', 'paper']


def is_hand(hand_input: str) -> TypeGuard[Hand]:
    """
    入力がじゃんけんの手として有効か判定

    :param hand_input: 入力文字列
    :return: True-> 有効 False-> 無効
    """
    if hand_input in hands:
        return True

    return False


def generate_hand() -> Hand:
    """
    じゃんけんの手を生成

    :return: じゃんけんの手
    """
    generated_hand_number = random.randint(0, len(hands) - 1)

    return hands[generated_hand_number]


def judge(user: Hand, cpu: Hand) -> None:
    """
    じゃんけんの勝敗判定

    :param user: ユーザの手
    :param cpu: 相手の手
    """
    # あいこ
    if user == cpu:
        print('DRAW')
        return

    hand_numbers = {'rock': 0, 'paper': 1, 'scissors': 2, 'tail': 3}

    # 勝ち
    # ユーザの手と相手の手を数値化したときの差が「1」であるとき、ユーザの勝利 先頭はそのままでは直前と比較できないのでローテーション
    is_user_win = hand_numbers[user] - hand_numbers[cpu] == 1
    if user == 'rock':
        is_user_win = hand_numbers['tail'] - hand_numbers[cpu] == 1

    if is_user_win:
        print('YOU WIN!!')
        return

    # 負け
    print('YOU LOSE...')


def main():
    while True:
        hand_input = input('じゃんけんの手を入力してください(ENDで終了)')

        if hand_input == 'END':
            return

        if not is_hand(hand_input):
            print('rock, scissors, paper, ENDのいずれかを入力してください。')
            continue

        # 型ガードにより、hand_inputはHand型であることが保証される
        # しかし、PyCharmではまだ型ガードをサポートしていないっぽいので、補足しておく
        user_hand = hand_input
        cpu_hand = generate_hand()
        judge(user_hand, cpu_hand)


if __name__ == '__main__':
    main()
