# 二分探索
import math
from typing import List, Optional

import input_integer


def search_binary_front(search_list: List[int], target: int) -> Optional[int]:
    """
    前方へ二分探索

    :param search_list: 探索元リスト
    :param target: 探索対象
    :return: 探索対象あり-> リスト内インデックス なし->None
    """
    head = 0
    tail = len(search_list) - 1

    while head <= tail:
        mid = math.floor((head + tail) / 2)
        print(f'mid is: {mid}')

        if search_list[mid] == target:
            return mid

        head = mid + 1

    return None


def search_binary_back(search_list: List[int], target: int) -> Optional[int]:
    """
    後方へ二分探索

    :param search_list: 探索元リスト
    :param target: 探索対象
    :return: 探索対象あり-> リスト内インデックス なし->None
    """
    head = 0
    tail = len(search_list) - 1

    while head <= tail:
        mid = math.floor((head + tail) / 2)
        print(f'mid is: {mid}')

        if search_list[mid] == target:
            return mid

        tail = mid - 1

    return None


def search_binary(search_list: List[int], target: int) -> Optional[int]:
    """
    二分探索

    :param search_list: 探索元リスト
    :param target: 探索対象
    :return: 探索対象あり-> リスト内インデックス なし->None
    """
    head = 0
    tail = len(search_list) - 1

    while head <= tail:
        mid = math.floor((head + tail) / 2)
        print(f'mid is: {mid}')

        if search_list[mid] == target:
            return mid

        if search_list[mid] < target:
            head = mid + 1
            continue

        if search_list[mid] > target:
            tail = mid - 1
            continue

    return None


def main():
    search_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = input_integer.get_integer_input()

    # target_index = search_binary_front(search_list, target)
    # target_index = search_binary_back(search_list, target)
    target_index = search_binary(search_list, target)

    if target_index is None:
        print(f'{target}は見つかりませんでした。')
        return

    print(f'{target}は、リストの{target_index}番目に存在します。')


if __name__ == '__main__':
    main()
