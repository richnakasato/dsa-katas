import random

def merge(arr, left, right):
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i+=1
        else:
            arr[k] = right[j]
            j+=1
        k+=1
    while i < len(left):
        arr[k] = left[i]
        i+=1
        k+=1
    while j < len(right):
        arr[k] = right[j]
        j+=1
        k+=1
    return arr

def mergesort(arr):
    if not arr or len(arr) < 2:
        return arr
    else:
        mid = len(arr)//2
        left = mergesort(arr[:mid])
        right = mergesort(arr[mid:])
        new_arr = [None] * len(arr)
        merge(new_arr, left, right)
        return new_arr


def main():
    lo = 0
    hi = 100
    n = 10
    arr = [random.randint(lo, hi) for _ in range(n)]
    arr_sort = sorted(arr[:])
    assert mergesort(arr)==arr_sort

if __name__ == "__main__":
    main()

