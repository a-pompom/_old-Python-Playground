# 挿入ソートの作成

from typing import List


def sort_by_insertion(unsorted_list: List[int]) -> List[int]:
    """
    挿入ソート

    :param unsorted_list: 対象リスト
    :return: ソート済みリスト
    """
    sort_list = list.copy(unsorted_list)

    for i in range(0, len(sort_list) - 1):
        for j in range(i + 1, 0, -1):

            # 対象要素 < ソート済みの要素の場合は、昇順となるよう入れ替えが必要
            if sort_list[j] < sort_list[j - 1]:
                sort_list[j], sort_list[j - 1] = sort_list[j - 1], sort_list[j]

    return sort_list


def main():
    unsorted_list = [5, 3, 4, 1, 2]
    print(sort_by_insertion(unsorted_list))


if __name__ == '__main__':
    main()
