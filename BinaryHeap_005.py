# leg 1 - 11:52:13
# leg 2 - 16:12:20
# TTC: 28:04:33
#

import random

class BinaryHeap(object):

    def __init__(self):
        self.data = [None]
        self.size = 0

    def __len__(self):
        return self.size

    def __str__(self):
        prefix = "size: " + str(self.size) + " -> "
        elements = [str(x) for x in self.data[1:]]
        return prefix + str(elements)

    def _pref_a(self, a, b):
        return self.data[a] < self.data[b]

    def _swap(self, a, b):
        self.data[a], self.data[b] = self.data[b], self.data[a]

    def _sift_up(self, idx):
        parent = idx//2
        if parent and self._pref_a(idx, parent):
            self._swap(idx, parent)
            self._sift_up(parent)

    def _sift_down(self, idx):
        left = idx * 2
        right = (idx * 2) + 1
        min = idx
        if left <= self.size and self._pref_a(left, min):
            min = left
        if right <= self.size and self._pref_a(right, min):
            min = right
        if min != idx:
            self._swap(min, idx)
            self._sift_down(min)

    def insert(self, item):
        self.data.append(item)
        self.size += 1
        self._sift_up(self.size)

    def peek(self):
        val = None
        if self.size:
            val = self.data[1]
        return val

    def remove(self):
        val = None
        if self.size:
            val = self.data[1]
            temp = self.data.pop()
            self.size -= 1
        if self.size:
            self.data[1] = temp
            self._sift_down(1)
        return val

    def build(self, arr):
        self.data = [None] + arr[:]
        self.size = len(arr)
        unsifted_parent = self.size//2
        while unsifted_parent:
            self._sift_down(unsifted_parent)
            unsifted_parent -= 1


def main():

    arr = random.sample(range(100), 10)
    print(arr)

    bh = BinaryHeap()
    print(bh)

    bh.build(arr)
    print(bh)

    for _ in range(len(arr)):
        print(bh.peek())
        print(bh)
        print(bh.remove())
        print(bh)

    for item in arr:
        bh.insert(item)
        print(bh)

if __name__ == "__main__":
    main()

