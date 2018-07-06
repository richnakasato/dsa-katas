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
        swapped = True
        curr_idx = idx
        while swapped:
            swapped = False
            left = (curr_idx*2)+1
            right = (curr_idx*2)+2
            if left < size and HeapSort._pref_left(items, left, curr_idx):
                curr_idx = left
                swapped = True
            if right < size and HeapSort._pref_left(items, right, curr_idx):
                curr_idx = right
                swapped = True
            if swapped:
                HeapSort._swap(items, curr_idx, idx)
                idx = curr_idx

    @staticmethod
    def sort(items):
        size = len(items)
        heapify_from = size // 2
        while heapify_from >= 0:
            HeapSort._sift_down(items, size, heapify_from)
            heapify_from -= 1
        num_unsorted = size
        while num_unsorted > 1:
            next_sorted_idx = num_unsorted - 1
            HeapSort._swap(items, 0, next_sorted_idx)
            num_unsorted -= 1
            HeapSort._sift_down(items, num_unsorted, 0)


def main():
    arr = random.sample(range(100), 10)
    print(arr)
    HeapSort.sort(arr)
    print(arr)

if __name__ == "__main__":
    main()

