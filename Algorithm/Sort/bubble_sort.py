# バブルソート

from typing import List


def sort_by_bubble(unsorted_list: List[int]) -> List[int]:
    """
    バブルソート

    :param unsorted_list: ソート対象リスト
    :return: ソート済みリスト
    """
    sort_list = list.copy(unsorted_list)

    # 全要素並べ替え済みとなるまで
    for i in range(0, len(sort_list) - 1):

        for j in range(len(sort_list) - 1, i, -1):
            # 小さいものを順に左へ寄せていくことで、昇順へ並び替え
            # 順々に要素が移動していく様が泡のように見えることから、バブルソートと名付けられた
            right = sort_list[j]
            left = sort_list[j - 1]

            if left > right:
                sort_list[j], sort_list[j-1] = sort_list[j-1], sort_list[j]

    return sort_list


def main():
    unsorted_list = [5, 3, 4, 1, 2]
    print(sort_by_bubble(unsorted_list))


if __name__ == '__main__':
    main()
