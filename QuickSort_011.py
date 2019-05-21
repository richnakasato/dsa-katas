import random

def partition(arr, lo, hi):
    tail = hi-1
    pivot = arr[tail]
    p_idx = lo
    for i in range(lo, hi):
        if arr[i] < pivot:
            arr[p_idx], arr[i] = arr[i], arr[p_idx]
            p_idx += 1
    arr[p_idx], arr[tail] = arr[tail], arr[p_idx]
    return p_idx


def quicksort(arr, lo, hi):
    if lo < hi:
        p_idx = partition(arr, lo, hi)
        quicksort(arr, lo, p_idx)
        quicksort(arr, p_idx+1, hi)


def main():
    lo = 0
    hi = 100
    n = 10
    arr = [random.randint(lo, hi) for _ in range(n)]
    arr_sort = sorted(arr[:])
    quicksort(arr, 0, n)
    assert arr==arr_sort

if __name__ == "__main__":
    main()

