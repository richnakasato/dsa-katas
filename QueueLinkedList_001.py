'''
Queue implementation using singly linked lists.

Interface and run times:
- enqueue(item) -> O(1)
- dequeue()     -> O(1)
- size()        -> O(1)

Time to implement:
- start         -> 20:03
- duration      ->

'''

import random

class Queue():

    class Node():

        def __init__(self, data=None, next_=None):
            self.data = data
            self.next = next_

        def __str__(self):
            return "{}->".format(self.data)


    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        outlist = list()
        outlist.append("size({}), head={}, tail={}: ".format(
            self.size,
            self.head,
            self.tail))
        curr = self.head
        while curr:
            outlist.append(str(curr))
            curr = curr.next
        outlist.append("NULL")
        return ''.join(outlist)

    def __len__(self):
        return self.size

    def enqueue(self, data):
        if not self.head:
            self.head = self.tail = self.Node(data)
        else:
            self.tail.next = self.Node(data)
            self.tail = self.tail.next
        self.size += 1

    def dequeue(self):
        if not self.head:
            raise Exception('queue is empty!')
        else:
            temp = self.head
            self.head = self.head.next
            self.size -= 1
            if not self.size:
                self.tail = None
            return temp


def main():
    lo = 1
    hi = 20
    n = 10
    arr = [random.randint(lo, hi) for x in range(n)]
    print(arr)
    q = Queue()
    print(q)
    for i in range(n):
        q.enqueue(arr[i])
    print(q)
    for i in range(n):
        print(q)
        print(q.dequeue())
    print(q)


if __name__ == "__main__":
    main()

