import os

# 期待結果を読み取るパス
dir_path = os.path.dirname(os.path.realpath(__file__))


def get_board(file_name: str) -> str:
    with open(f'{dir_path}/{file_name}') as f:
        return f.read()


def get_initial_board() -> str:
    return get_board('initialBoard.txt')


def get_single_1p_board() -> str:
    return get_board('single1PBoard.txt')


def get_single_both_player_board() -> str:
    return get_board('singleBothPlayerBoard.txt')


def get_multiple_both_player_board() -> str:
    return get_board('multipleBothPlayerInput.txt')
