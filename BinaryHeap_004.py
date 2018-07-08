# TTC -
import random

class BinaryHeap(object):

    def __init__(self):
        self.data = [None]
        self.size = 0

    def __str__(self):
        return 'size: ' + str(self.size) + ', ' + ' '.join([str(x) for x in self.data[1:]])

    def __len__(self):
        return self.size

    def _swap(self, a, b):
        self.data[a], self.data[b] = self.data[b], self.data[a]

    def _sift_up(self, idx):
        if idx // 2:
            if self.data[idx//2] < self.data[idx]:
                self._swap(idx//2, idx)
                self._sift_up(idx//2)

    def _sift_down(self, idx):
        min_idx = idx
        if idx*2 <= self.size and self.data[min_idx] > self.data[idx*2]:
            min_idx = idx*2
        if (idx*2)+1 <= self. size and self.data[min_idx] > self.data[idx*2+1]:
            min_idx = (idx*2)+1
        if min_idx != idx:
            self._swap(min_idx, idx)
            self._sift_down(min_idx)

    def insert(self, item):
        self.data.append(item)
        self.size += 1
        self._sift_up(self.size)

    def peek(self):
        if self.size:
            return self.data[1]
        else:
            return None

    def remove(self):
        temp = None
        if self.size:
            temp = self.data[1]
            self.size -= 1
            if self.size:
                self.data[1] = self.data.pop()
                self._sift_down(1)
            else:
                self.data.pop()
        return temp

    def build(self, items):
        self.data = [None] + items[:]
        self.size = len(items)
        idx = self.size//2
        while idx:
            self._sift_down(idx)
            idx-=1

    def sort(self, items):
        self.build(items)
        size = self.size
        while self.size > 1:
            self._swap(1, self.size)
            self.size -= 1
            self._sift_down(1)
        self.size = size

def main():
    arr = random.sample(range(100), 10)
    print(arr)
    bh = BinaryHeap()
    bh.build(arr)
    print(bh)
    print(bh.peek())
    print(len(bh))
    for count in range(len(arr)):
        print(str(bh.remove()))
    print(len(bh))

    arr_sort = random.sample(range(100), 10)
    bh_sort = BinaryHeap()
    bh_sort.sort(arr_sort)
    print(arr_sort)
    print(bh_sort)


if __name__ == "__main__":
    main()
