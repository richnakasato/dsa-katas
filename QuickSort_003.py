import random

def swap(A, i, j):
    A[i], A[j] = A[j], A[i]

def partition(A, start, end):
    pivot = A[end]
    p_idx = start
    for i in range(start, end):
        if A[i] < pivot:
            swap(A, i, p_idx)
            p_idx += 1
    swap(A, end, p_idx)
    return p_idx

def quicksort(A, start, end):
    if start < end:
        p_idx = partition(A, start, end)
        quicksort(A, start, p_idx-1)
        quicksort(A, p_idx+1, end)


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

