class BinaryHeap():

    def __init__(self):
        self.elements = [0]
        self.size = 0

    def __str__(self):
        if self.size:
            return ' '.join([str(x) for x in self.elements[1:]])
        else:
            return "Heap is empty!"

    def insert(self, val):
        self.elements.append(val)
        self.size += 1
        self._sift_up(self.size)

    def find_min(self):
        if self.size:
            return self.elements[1]
        raise Exception("Heap is empty!")

    def remove_min(self):
        if self.size:
            min_val = self.elements[1]
            self.elements[1] = self.elements.pop()
            self.size -= 1
            self._sift_down(1)
            return min_val
        raise Exception("Heap is empty!")

    def build_heap(self, val_array):
        pass

    def _swap(self, a_idx, b_idx):
        self.elements[a_idx], self.elements[b_idx] = \
                self.elements[b_idx], self.elements[a_idx]

    def _min_child(self, idx):
        if (idx * 2 + 1) > self.size:
            return idx * 2
        else:
            if self.elements[idx * 2] < self.elements[idx * 2 + 1]:
                return idx * 2
            else:
                return idx * 2 + 1

    def _sift_up(self, idx):
        while (idx // 2) > 0:
            if self.elements[idx] < self.elements[idx // 2]:
                self._swap(idx, idx // 2)
            idx //= 2

    def _sift_down(self, idx):
        while (idx * 2) <= self.size:
            min_child = self._min_child(idx)
            if self.elements[idx] > self.elements[min_child]:
                self._swap(idx, min_child)
            idx = min_child


def main():
    mh = BinaryHeap()
    mh.insert(8)
    print(mh)
    mh.insert(3)
    print(mh)
    mh.insert(9)
    print(mh)
    mh.insert(1)
    print(mh)
    print(mh.find_min())
    print(mh.size)

    mh.remove_min()
    print(mh)
    mh.remove_min()
    print(mh)
    print(mh.size)

if __name__ == "__main__":
    main()

