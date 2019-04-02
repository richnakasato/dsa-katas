import random

def partition(arr, start, end):
    pivot = arr[end-1]
    pidx = start
    for i in range(start, end):
        if arr[i] < pivot:
            arr[i], arr[pidx] = arr[pidx], arr[i]
            pidx += 1
    arr[pidx], arr[end-1] = arr[end-1], arr[pidx]
    return pidx


def quicksort(arr, start, end):
    if start < end:
        pidx = partition(arr, start, end)
        quicksort(arr, start, pidx)
        quicksort(arr, pidx+1, end)
    return


def main():
    lo = 0
    hi = 100
    n = 10
    arr = [random.randint(lo, hi) for _ in range(n)]
    arr_sort = sorted(arr[:])
    quicksort(arr, 0, len(arr))
    assert arr==arr_sort

if __name__ == "__main__":
    main()

