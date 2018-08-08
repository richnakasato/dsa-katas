'''
Practicing SLL, no timing
'''
import random

class SinglyLinkedList:

    class Node:

        def __init__(self, data):
            self.data = data
            self.next = None


    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def print(self):
        curr = self.head
        while curr:
            print(curr.data, end=' ')
            curr = curr.next
        print()

    def prepend(self, data):
        temp = self.Node(data)
        temp.next = self.head
        self.head = temp

    def append(self, data):
        if not self.head:
            self.head = self.Node(data)
        else:
            self.head = self._append(self.head, data)

    def _append(self, curr, data):
        if not curr:
            return self.Node(data)
        else:
            curr.next = self._append(curr.next, data)
            return curr

    def insert(self, data, idx):
        if not self.head and idx == 0:
            temp = self.Node(data)
            temp.next = self.head
            self.head = temp
        else:
            self.head = self._insert(self.head, data, idx)

    def _insert(self, curr, data, idx):
        if not curr and idx > 0:
            raise Exception('index out of bounds!')
        if not curr and idx == 0:
            return self.Node(data)
        if idx == 0:
            temp = self.Node(data)
            temp.next = curr
            return temp
        else:
            curr.next = self._insert(curr.next, data, idx - 1)
            return curr


def main():
    arr = random.sample(range(100), 10)
    print(arr)

    sll = SinglyLinkedList()
    for item in arr:
        sll.prepend(item)
        sll.print()

    sll2 = SinglyLinkedList()
    for item in arr:
        sll2.append(item)
        sll2.print()

    sll2.insert(99, 5)
    sll2.insert(99, 0)
    sll2.insert(99, 11)
    sll2.insert(99, 13)
    sll2.print()

if __name__ == "__main__":
    main()
