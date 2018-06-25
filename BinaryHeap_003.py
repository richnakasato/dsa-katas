import random
# Time-To-Complete = 34:03:73

class BinaryHeap(object):

    def __init__(self):
        self.elem = [None]
        self.size = 0

    def __str__(self):
        if not self.size:
            return 'Empty!'
        else:
            return ' '.join([str(x) for x in self.elem[1:]])

    def _swap(self, ai, bi):
        self.elem[ai], self.elem[bi] = self.elem[bi], self.elem[ai]

    def _sift_up(self, idx):
        while idx // 2:
            if self.elem[idx] < self.elem[idx//2]:
                self._swap(idx, idx//2)
            idx //= 2

    def _min_child(self, idx):
        if idx * 2 + 1 > self.size:
            return idx * 2
        else:
            if self.elem[idx*2] < self.elem[idx*2+1]:
                return idx * 2
            else:
                return idx * 2 + 1

    def _sift_down(self, idx):
        while idx * 2 <= self.size:
            min_child = self._min_child(idx)
            if self.elem[min_child] < self.elem[idx]:
                self._swap(idx, min_child)
            idx = min_child

    def build_heap(self, arr):
        self.elem = [None] + arr[:]
        self.size = len(arr)
        idx = self.size // 2
        while idx:
            self._sift_down(idx)
            idx -= 1

    def push(self, data):
        self.elem.append(data)
        self.size += 1
        self._sift_up(self.size)

    def peek_min(self):
        if not self.size:
            return None
        else:
            return self.elem[1]

    def pop_min(self):
        if not self.size:
            return None
        else:
            popped = self.elem[1]
            temp = self.elem.pop()
            self.size -= 1
            if self.size > 0:
                self.elem[1] = temp
                self._sift_down(1)
            return popped

    def sort(self):
        true_size = self.size
        while self.size > 1:
            sz = self.size
            self.elem[1], self.elem[sz] = self.elem[sz], self.elem[1]
            self.size -= 1
            self._sift_down(1)
        self.elem = [None] + self.elem[1:][::-1]


def main():
    arr = random.sample(range(100), 10)
    print(arr)

    bh = BinaryHeap()
    bh.build_heap(arr)
    print(bh)
    for num in range(bh.size+1):
        print('peeking: ' + str(bh.peek_min()))
        print('popping: ' + str(bh.pop_min()))
    bh.sort()
    print(bh)

    arr = random.sample(range(100), 10)
    print(arr)
    bh2 = BinaryHeap()
    for item in arr:
        bh2.push(item)
        print(bh2)
    bh2.sort()
    print(bh2)

if __name__ == "__main__":
    main()

