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

    def __str__(self):
        if not self.head:
            return 'Empty!'
        else:
            return self._str(self.head)

    def _str(self, curr):
        if not curr:
            return ''
        else:
            return str(curr.data) + ' ' + self._str(curr.next)

    def prepend(self, data):
        temp = self.Node(data)
        temp.next = self.head
        self.head = temp
        self.size += 1

    def append(self, data):
        if not self.head:
            self.size += 1
            self.head = self.Node(data)
        else:
            self.head = self._append(self.head, data)

    def _append(self, curr, data):
        if not curr:
            self.size += 1
            return self.Node(data)
        else:
            curr.next = self._append(curr.next, data)
            return curr

    def insert(self, data, idx):
        if not self.head and idx == 0:
            temp = self.Node(data)
            temp.next = self.head
            self.head = temp
            self.size += 1
        else:
            self.head = self._insert(self.head, data, idx)

    def _insert(self, curr, data, idx):
        if not curr:
            if idx == 0:
                self.size += 1
                return self.Node(data)
            else:
                raise Exception('index out of bounds!')
        else:
            if idx == 0:
                temp = self.Node(data)
                temp.next = curr
                self.size += 1
                return temp
            else:
                curr.next = self._insert(curr.next, data, idx - 1)
                return curr

    def pop_left(self):
        if not self.head:
            return None
        else:
            temp = self.head.data
            self.head = self.head.next
            self.size -= 1
            return temp

    def pop_right(self):
        if not self.head:
            return None
        else:
            self.head, data = self._pop_right(self.head)
            return data

    def _pop_right(self, curr):
        if not curr:
            return None, None
        else:
            if not curr.next:
                self.size -= 1
                return None, curr.data
            else:
                curr.next, data = self._pop_right(curr.next)
                return curr, data

    def pop_at(self, idx):
        if not self.head:
            raise Exception('list is empty!')
        else:
            self.head, data = self._pop_at(self.head, idx)
            return data

    def _pop_at(self, curr, idx):
        if not curr:
            return None, None
        else:
            if idx == 0:
                self.size -= 1
                return curr.next, curr.data
            else:
                curr.next, data = self._pop_at(curr.next, idx - 1)
                return curr, data

    def pop_value(self, data):
        if not self.head:
            raise Exception('list is empty!')
        else:
            self.head = self._pop_value(self.head, data)

    def _pop_value(self, curr, data):
        if not curr:
            return None
        else:
            if curr.data == data:
                self.size -= 1
                return curr.next
            else:
                curr.next = self._pop_value(curr.next, data)
                return curr


def main():
    arr = random.sample(range(100), 10)
    print(arr)

    sll = SinglyLinkedList()
    for item in arr:
        sll.prepend(item)
        print(sll)
        print(len(sll))

    sll2 = SinglyLinkedList()
    for item in arr:
        sll2.append(item)
        print(sll2)
        print(len(sll2))

    sll2.insert(99, 5)
    sll2.insert(99, 0)
    sll2.insert(99, 11)
    sll2.insert(99, 13)
    print(sll2)
    print(len(sll2))

    print('removing...')
    while len(sll):
        #print(sll.pop_left())
        print(sll.pop_right())


if __name__ == "__main__":
    main()

