'''
TTC: 53:24:71

Issues:
    1) Need to remember how to do iter sift down
    2) Need to remember to check for while len >= 0 when using 0 idx in heap
    3) Sift down for HeapSort needs to take in length to sift down to (for
    inplace sorting)
'''
import random

class HeapSort:

    @staticmethod
    def _swap(arr, a, b):
        arr[a], arr[b] = arr[b], arr[a]

    @staticmethod
    def _pref_idx(arr, a, b):
        if arr[a] > arr[b]:
            return a
        else:
            return b

    @staticmethod
    def _get_children(idx):
        return (idx * 2) + 1, (idx * 2) + 2

    @staticmethod
    def _get_parent(idx):
        return (idx - 1) // 2

    @staticmethod
    def _sift_down_iter(arr, idx, length):
        continue_sifting = True
        while(continue_sifting):
            pref_idx = idx
            left_idx, right_idx = HeapSort._get_children(idx)
            if left_idx < length and HeapSort._pref_idx(arr, pref_idx, left_idx) == left_idx:
                pref_idx = left_idx
            if right_idx < length and HeapSort._pref_idx(arr, pref_idx, right_idx) == right_idx:
                pref_idx = right_idx
            if pref_idx == idx:
                continue_sifting = False
            else:
                HeapSort._swap(arr, pref_idx, idx)
                idx = pref_idx

    @staticmethod
    def _sift_down_recur(arr, idx, length):
        pref_idx = idx
        left_idx, right_idx = HeapSort._get_children(idx)
        if left_idx < length and HeapSort._pref_idx(arr, pref_idx, left_idx) == left_idx:
            pref_idx = left_idx
        if right_idx < length and HeapSort._pref_idx(arr, pref_idx, right_idx) == right_idx:
            pref_idx = right_idx
        if pref_idx != idx:
            HeapSort._swap(arr, pref_idx, idx)
            HeapSort._sift_down_recur(arr, pref_idx)

    @staticmethod
    def sort(arr):
        curr_idx = HeapSort._get_parent(len(arr))
        while curr_idx >= 0:
            HeapSort._sift_down_iter(arr, curr_idx, len(arr))
            curr_idx -= 1
        working_len = len(arr)
        while working_len:
            HeapSort._swap(arr, 0, working_len - 1)
            working_len -= 1
            HeapSort._sift_down_iter(arr, 0, working_len)


def main():
    arr = random.sample(range(100), 10)
    print arr

    HeapSort.sort(arr)
    print arr

if __name__ == "__main__":
    main()
