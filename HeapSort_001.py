# TTC: ~30 minutes
import random

class HeapSort(object):

    @staticmethod
    def _swap(items, left, right):
        items[left], items[right] = items[right], items[left]

    @staticmethod
    def _pref_left(items, left, right):
        return items[left] > items[right]

    @staticmethod
    def _sift_down(items, size, idx):
        pref_idx = idx
        if (idx*2)+1 < size and HeapSort._pref_left(items, (idx*2)+1, pref_idx):
            pref_idx = (idx*2)+1
        if (idx*2)+2 < size and HeapSort._pref_left(items, (idx*2)+2, pref_idx):
            pref_idx = (idx*2)+2
        if pref_idx != idx:
            HeapSort._swap(items, pref_idx, idx)
            HeapSort._sift_down(items, size, pref_idx)

    @staticmethod
    def sort(items):
        size = len(items)
        heapify_from = size // 2
        while heapify_from >= 0:
            HeapSort._sift_down(items, size, heapify_from)
            heapify_from -= 1
        unsorted = size
        while unsorted:
            HeapSort._swap(items, 0, unsorted-1)
            unsorted -= 1
            HeapSort._sift_down(items, unsorted, 0)


def main():
    arr = random.sample(range(100), 10)
    print(arr)
    HeapSort.sort(arr)
    print(arr)

if __name__ == "__main__":
    main()

