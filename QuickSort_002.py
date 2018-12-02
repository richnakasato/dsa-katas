import random

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def partition(arr, start, end):
    pivot = arr[end]
    p_idx = start
    for i in range(start, end):
        if arr[i] < pivot:
            swap(arr, i, p_idx)
            p_idx += 1
    swap(arr, p_idx, end)
    return p_idx

def quicksort(arr, start, end):
    if start < end:
        p_idx = partition(arr, start, end)
        quicksort(arr, start, p_idx-1)
        quicksort(arr, p_idx+1, end)


def main():
    lo = 0
    hi = 100
    n = 10
    arr = [random.randint(lo, hi) for _ in range(n)]
    arr_sort = sorted(arr[:])
    quicksort(arr, 0, len(arr)-1)
    assert arr==arr_sort

if __name__ == "__main__":
    main()

