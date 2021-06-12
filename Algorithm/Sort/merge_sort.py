import math
from typing import List


def merge_list(left: List[int], right: List[int]) -> List[int]:
    """
    2つのサブリストをマージ

    :param left: 左のリスト
    :param right: 右のリスト
    :return: マージ済みリスト 昇順にソート済み
    """
    merged = []

    while True:
        # すべてマージ済みとなったら、マージ結果を返却
        if len(left) == 0 and len(right) == 0:
            return merged

        # マージ元のサブリストはソート済みなので、大小比較の結果片側が空となった後は、
        # 残ったものをそのままマージ結果へ格納することでソート済みリストが得られる
        if len(left) == 0:
            merged.append(right.pop(0))
            continue
        if len(right) == 0:
            merged.append(left.pop(0))
            continue

        # 左右のサブリストから、小さいものをマージ結果へ格納
        # これを繰り返せば、マージ結果がソート済みとなる
        if left[0] < right[0]:
            merged.append(left.pop(0))
            continue
        if left[0] > right[0]:
            merged.append(right.pop(0))
            continue


def sort_by_merge(source_list: List[int]) -> List[int]:
    """
    マージソート

    :param source_list: 対象リスト
    :return: ソート済みリスト
    """

    # 要素数が1であれば、既にソート済みなので、対象リストをそのまま返却
    if len(source_list) == 1:
        return source_list

    # 単体の要素になるまで左右に分割
    center = math.floor(len(source_list) / 2)
    left = source_list[:center]
    right = source_list[center:]

    left = sort_by_merge(left)
    right = sort_by_merge(right)

    # 左右のサブリストをマージすることで、ソート済みリストを得る
    # マージ結果を呼び出し元へ返却し、繰り返しマージすることで、リスト全体がソート済みとなる
    return merge_list(left, right)


def main():
    source_list = [8, 7, 5, 3, 1, 6, 4, 9, 2]

    print(sort_by_merge(source_list))


if __name__ == '__main__':
    main()
