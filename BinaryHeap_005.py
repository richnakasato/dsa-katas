# leg 1 - 11:52:13
# TTC:
#
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

    def _pref_a(a, b):
        return a < b

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
        pass

    def peek(self):
        pass

    def remove(self):
        pass

    def build(self, arr):
        pass


def main():
    bh = BinaryHeap()
    print(bh)
    pass

if __name__ == "__main__":
    main()

