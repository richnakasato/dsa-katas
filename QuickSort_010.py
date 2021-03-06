import random

def partition(arr, start, end):
    tail = end - 1
    pivot = arr[tail]
    p_idx = start
    for i in range(start, end):
        if arr[i] < pivot:
            arr[p_idx], arr[i] = arr[i], arr[p_idx]
            p_idx += 1
    arr[p_idx], arr[tail] = arr[tail], arr[p_idx]
    return p_idx


def quicksort(arr, start, end):
    if start < end:
        p_idx = partition(arr, start, end)
        left = quicksort(arr, start, p_idx)
        right = quicksort(arr, p_idx+1, end)
    return


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

