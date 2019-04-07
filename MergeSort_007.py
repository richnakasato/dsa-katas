import random

def merge(left, right):
    res = [None] * (len(left) + len(right))
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res[k] = left[i]
            i += 1
        else:
            res[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        res[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        res[k] = right[j]
        j += 1
        k += 1
    return res


def mergesort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    merged = merge(left, right)
    return merged


def main():
    lo = 0
    hi = 100
    n = 10
    arr = [random.randint(lo, hi) for _ in range(n)]
    arr_sort = sorted(arr[:])
    assert mergesort(arr)==arr_sort


if __name__ == "__main__":
    main()

