# 選択ソート

from typing import List


def sort_by_selection(unsorted_list: List[int]) -> List[int]:
    """
    選択ソート

    :param unsorted_list: ソート対象リスト
    :return: ソート済みリスト
    """
    sort_list = list.copy(unsorted_list)

    # 全要素並べ替え済みとなるまで
    for i in range(0, len(sort_list) - 1):

        # リスト内から最小値を「選択」
        min_index = None
        for j in range(i, len(sort_list)):
            if min_index is None:
                min_index = j
                continue

            if sort_list[min_index] > sort_list[j]:
                min_index = j

        # 入れ替え
        sort_list[i], sort_list[min_index] = sort_list[min_index], sort_list[i]

    return sort_list


def main():
    unsorted_list = [5, 3, 4, 1, 2]
    print(sort_by_selection(unsorted_list))


if __name__ == '__main__':
    main()
