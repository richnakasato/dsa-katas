import random

def merge(left, right):
    len_left = len(left)
    len_right = len(right)
    merged = [None] * (len_left + len_right)
    i = j = k = 0
    while i < len_left and j < len_right:
        if left[i] < right[j]:
            merged[k] = left[i]
            i+=1
        else:
            merged[k] = right[j]
            j+=1
        k+=1
    while i < len_left:
        merged[k] = left[i]
        i+=1
        k+=1
    while j < len_right:
        merged[k] = right[j]
        j+=1
        k+=1
    return merged


def mergesort(arr):
    len_arr = len(arr)
    if len_arr < 2:
        return arr
    else:
        mid = len_arr//2
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

