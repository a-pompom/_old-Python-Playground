import os

# 期待結果を読み取るパス
dir_path = os.path.dirname(os.path.realpath(__file__))


def get_initial_board() -> str:
    with open(f'{dir_path}/expectedInitialBoard.txt') as f:
        return f.read()
