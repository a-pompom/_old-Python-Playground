# キューの作成
# 関数でやってもあまり手応えはなかったので、クラス・連結リストのみやるか
from typing import Any, Optional


class QueueLinkedList:
    """ 連結リストでキューを実現 """

    def __init__(self, item: Any = None):
        self.item = item
        self.next: Optional[QueueLinkedList] = None

    def enqueue(self, item: Any):
        """
        キューへ要素を追加
        先頭は要素を持たず、次の要素への参照のみを保持

        :param item: 追加要素
        """
        print(f'enqueue: {item}')
        current = self

        while current.next is not None:
            current = current.next

        queue = QueueLinkedList(item)
        current.next = queue

    def dequeue(self):
        """
        キューから要素を取り出し

        :return: 取り出した要素
        """
        # 空判定
        if self.next is None:
            print('queue is empty...')
            return

        item = self.next.item
        print(f'dequeue: {item}')
        # 先頭が指す参照を一つ先へ切り替えることで、削除を実現
        self.next = self.next.next

        return item


class Queue:
    """ キューのデータ構造を責務に持つ """

    def __init__(self):
        self.queue = []

    def enqueue(self, item: Any):
        """
        キューへ要素を追加
        :param item: 追加要素
        :return:
        """
        print(f'enqueue: {item}')
        self.queue.append(item)

    def dequeue(self) -> Any:
        """
        キューから要素を取り出す
        :return: 取り出した要素
        """
        # 空判定
        if len(self.queue) == 0:
            print('queue is empty...')
            return None

        item = self.queue[0]
        print(f'dequeue: {item}')
        del self.queue[0]

        return item


def main():
    print('normal queue')
    queue = Queue()

    queue.enqueue(10)
    queue.enqueue(100)
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()

    print('linked list queue')
    linked_queue = QueueLinkedList()
    linked_queue.enqueue('item1')
    linked_queue.enqueue('item2')
    linked_queue.enqueue('item3')
    linked_queue.dequeue()
    linked_queue.dequeue()
    linked_queue.dequeue()
    linked_queue.dequeue()


if __name__ == '__main__':
    main()
