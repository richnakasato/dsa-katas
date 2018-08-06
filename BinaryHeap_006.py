'''

TTC: 39.22.47

1) Had issues with sift down! Wasn't sure how to implement it... took a lot of
time
2) Remove also caused some problems with going from 1 to 0 size and when to pop
and push into data[1]

'''
import random

class BinaryHeap:

    def __init__(self):
        self.data = [None]
        self.size = 0

    def __len__(self):
        return self.size

    def __str__(self):
        return 'Size:' + str(self.size) + ' --> ' + str(self.data[1:])

    def _pref_left(self, a, b):
        return self.data[a] < self.data[b]

    def _pref_idx(self, a, b):
        if self._pref_left(a, b):
            return a
        else:
            return b

    def _swap(self, a, b):
        self.data[a], self.data[b] = self.data[b], self.data[a]

    def _sift_up(self, idx):
        parent = idx // 2
        if parent:
            pref_idx = self._pref_idx(parent, idx)
            if pref_idx != parent:
                self._swap(parent, idx)
                self._sift_up(parent)

    def _sift_down(self, idx):
        pref_idx = idx
        left_idx = idx * 2
        right_idx = (idx * 2) + 1
        if left_idx <= self.size and self._pref_idx(pref_idx, left_idx) != pref_idx:
            pref_idx = left_idx
        if right_idx <= self.size and self._pref_idx(pref_idx, right_idx) != pref_idx:
            pref_idx = right_idx
        if pref_idx != idx:
            self._swap(pref_idx, idx)
            self._sift_down(pref_idx)

    def insert(self, data):
        self.data.append(data)
        self.size += 1
        self._sift_up(self.size)

    def peek(self):
        if self.size:
            return self.data[1]
        else:
            return None

    def remove(self):
        ret_val = self.peek()
        temp = self.data.pop(self.size)
        if self.size - 1:
            self.data[1] = temp
        self.size -= 1
        self._sift_down(1)
        return ret_val

    def build(self, arr):
        self.data = [None] + arr[:]
        self.size = len(arr)
        sift_idx = self.size // 2
        while(sift_idx):
            self._sift_down(sift_idx)
            sift_idx -= 1


def main():
    arr = random.sample(range(100), 10)

    bh = BinaryHeap()
    bh.build(arr)
    print(bh)

    arr = random.sample(range(100), 10)
    bh2 = BinaryHeap()
    for item in arr:
        bh2.insert(item)
        print(bh2.peek())
        print(bh2)

    while(len(bh2)):
        print(bh2.remove())
        print(bh2)


if __name__ == "__main__":
    main()
