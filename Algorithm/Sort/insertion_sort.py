# 挿入ソートの作成

from typing import List


def sort_by_insertion(unsorted_list: List[int]) -> List[int]:
    sort_list = list.copy(unsorted_list)

    for i in range(0, len(sort_list) - 1):
        for j in range(i + 1, 0, -1):

            if sort_list[j] < sort_list[j - 1]:
                sort_list[j], sort_list[j - 1] = sort_list[j - 1], sort_list[j]

    return sort_list


def main():
    unsorted_list = [5, 3, 4, 1, 2]
    print(sort_by_insertion(unsorted_list))


if __name__ == '__main__':
    main()
