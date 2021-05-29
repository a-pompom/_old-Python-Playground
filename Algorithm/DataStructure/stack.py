# スタックをつくってみる

# とりあえず数値のみ
# リストを操作する関数の自作/クラスでスタックを実現するパターンをつくってみたい
# あらゆる型に対応可能な連結リストでも実装してみたいc
from typing import Any, Union


class StackLinkedList:
    """ スタックの単方向連結リスト版 """

    def __init__(self, item: Any = None):
        self.item = item
        self.next: Union[StackLinkedList, None] = None

    def push(self, item: Any):
        """
        スタックへ要素を追加

        :param item: 追加要素
        :return:
        """
        current = self

        while current.next is not None:
            current = current.next

        current.next = StackLinkedList(item)

    def pop(self) -> Any:
        """
        スタックから要素を取得

        :return: 取り出した要素
        """

        current = self
        # pop()は末尾の要素を削除
        # これは末尾の一つ前の要素の次の参照を空にする操作と等価
        prev = self

        while current.next is not None:
            prev = current
            current = current.next

        item = current.item
        prev.next = None

        return item


class Stack:
    """ データ構造Stackとしての動きを責務に持つ"""

    def __init__(self):
        self.stack = []

    def push(self, item: int) -> None:
        """
        スタックへ要素を追加

        :param item: 追加要素
        :return:
        """
        print(f'push: {item}')
        self.stack.append(item)

    def pop(self) -> int:
        """
        スタックから要素を抽出

        :return: スタックの末尾要素
        """

        item = self.stack[len(self.stack) - 1]
        print(f'{item} popped.')
        del self.stack[len(self.stack) - 1]

        return item


def push_stack(stack: list[int], item: int) -> None:
    """
    スタックへ要素を追加

    :param stack: 操作対象スタック
    :param item: 追加要素
    :return:
    """
    stack.append(item)


def pop_stack(stack: list[int]) -> int:
    """
    スタックから要素を取り出す

    :param stack: 操作対象スタック
    :return: 取り出した要素
    """
    item = stack[len(stack) - 1]
    del stack[len(stack) - 1]

    return item


def main():
    # 関数
    print('function stack')
    stack = [1, 2, 3, 4, 5]
    push_stack(stack, 6)
    print(f'stack: {stack}')
    print(f'pop stack: {pop_stack(stack)}')

    # クラス
    print('class stack')
    class_stack = Stack()
    class_stack.push(10)
    class_stack.push(100)
    class_stack.pop()

    # 連結リスト
    print('linked list stack')
    linked_stack = StackLinkedList()
    linked_stack.push('item1')
    linked_stack.push('item2')
    linked_stack.push('item3')
    print(f'{linked_stack.pop()} popped')
    print(f'{linked_stack.pop()} popped')
    print(f'{linked_stack.pop()} popped')


if __name__ == '__main__':
    main()
