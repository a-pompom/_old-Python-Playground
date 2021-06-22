# 線形探索
# 入力した数値がリストに存在するか探索
import input_integer
from typing import List, Optional


def search_linear(search_list: List[int], target: int) -> Optional[int]:
    """
    線形探索のアルゴリズムに則って探索
    :param search_list: 探索元リスト
    :param target: 探索対象
    :return: 合致あり-> リスト内のインデックス 合致なし-> None
    """
    for index, item in enumerate(search_list):
        if item == target:
            return index

    return None


def main():
    search_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    target = input_integer.get_integer_input()
    target_index = search_linear(search_list, target)

    if target_index is None:
        print(f'{target}は見つかりませんでした。')
        return

    print(f'{target}は、リストの{target_index}番目にあります。')


if __name__ == '__main__':
    main()
