# クイックソートを実装
from typing import List


def sort_by_pivot(source_list: List[int]) -> List[int]:
    """
    ピボットを利用したクイックソート

    :param source_list: ソート対象リスト
    :return: ソート済みリスト
    """

    # 要素数が1以下の場合、ピボットで分割する必要がないので、対象リストを返却
    # 当該リストは、後述のleft/rightへ格納されているので、呼び出し元でソート済みリストの要素として合成される
    if len(source_list) <= 1:
        return source_list

    # ピボットは簡単にするため、先頭を選択
    pivot = source_list[0]
    # 左側はピボットより小さい要素を・右側は大きい要素を格納
    left = []
    right = []

    # ピボットから要素を振り分け
    for item in source_list:
        if item < pivot:
            left.append(item)
            continue

        if item > pivot:
            right.append(item)
            continue

    # 左右それぞれへ同様にピボットによる分割を適用していく
    # その後、左→ピボット→右の順に並べれば、ソート済みリストが完成
    return sort_by_pivot(left) + [pivot] + sort_by_pivot(right)


def main():
    source_list = [5, 7, 9, 10, 6, 2, 3, 4, 8, 1]
    print(sort_by_pivot(source_list))


if __name__ == '__main__':
    main()
