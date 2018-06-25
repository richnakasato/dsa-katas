import random

class BinaryHeap():

    def __init__(self):
        self.elem = [0]
        self.size = 0

    def __str__(self):
        return ' '.join([str(x) for x in self.elem[1:]]) if self.size else 'Empty'

    def __len__(self):
        return self.size

    def _swap(self, ai, bi):
        self.elem[ai], self.elem[bi] = self.elem[bi], self.elem[ai]

    def _min_child_idx(self, idx):
        lci = idx * 2
        rci = idx * 2 + 1
        return lci if rci > self.size or self.elem[lci] < self.elem[rci] else rci

    def _sift_down(self, idx):
        while idx * 2 <= self.size:
            min_child = self._min_child_idx(idx)
            if self.elem[min_child] < self.elem[idx]:
                self._swap(min_child, idx)
            idx = min_child

    def _sift_up(self, idx):
        while idx // 2:
            if self.elem[idx] < self.elem[idx // 2]:
                self._swap(idx, idx // 2)
            idx //= 2

    def build_heap(self, arr):
        self.elem = [0] + arr[:]
        self.size = len(arr)
        idx = self.size // 2
        while idx:
            self._sift_down(idx)
            idx -= 1

    def insert(self, val):
        self.elem.append(val)
        self.size += 1
        self._sift_up(self.size)

    def peek_min(self):
        return self.elem[1] if self.size else None

    def remove_min(self):
        cur_min = self.peek_min()
        if self.size == 1:
            self.elem.pop()
            self.size -= 1
        elif self.size > 1:
            self.elem[1] = self.elem.pop()
            self.size -= 1
            self._sift_down(1)
        return cur_min


def main():
    bh = BinaryHeap()
    arr = random.sample(range(1, 100), 20)
    bh.build_heap(arr)
    print(bh)

    sort_arr = list()
    for x in xrange(len(bh)):
        sort_arr.append(bh.remove_min())

    print(sort_arr)

if __name__ == "__main__":
    main()

