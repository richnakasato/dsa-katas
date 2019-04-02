import random

def merge(arr_lhs, arr_rhs):
    lhs = 0
    rhs = 0
    arr_sorted = [None] * (len(arr_lhs) + len(arr_rhs))
    idx = 0
    while lhs < len(arr_lhs) and rhs < len(arr_rhs):
        if arr_lhs[lhs] < arr_rhs[rhs]:
            arr_sorted[idx] = arr_lhs[lhs]
            lhs += 1
        else:
            arr_sorted[idx] = arr_rhs[rhs]
            rhs += 1
        idx += 1
    while lhs < len(arr_lhs):
        arr_sorted[idx] = arr_lhs[lhs]
        lhs += 1
        idx += 1
    while rhs < len(arr_rhs):
        arr_sorted[idx] = arr_rhs[rhs]
        rhs += 1
        idx += 1
    return arr_sorted


def mergesort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left = mergesort(arr[0:mid])
    right = mergesort(arr[mid:len(arr)])
    res = merge(left, right)
    return res


def main():
    lo = 0
    hi = 100
    n = 10
    arr = [random.randint(lo, hi) for _ in range(n)]
    arr_sort = sorted(arr[:])
    assert mergesort(arr)==arr_sort

if __name__ == "__main__":
    main()

