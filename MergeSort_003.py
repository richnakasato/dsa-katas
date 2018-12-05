import random

def merge(merged, left, right):
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged[k] = left[i]
            i+=1
        else:
            merged[k] = right[j]
            j+=1
        k+=1
    while i < len(left):
        merged[k] = left[i]
        i+=1
        k+=1
    while j < len(right):
        merged[k] = right[j]
        j+=1
        k+=1
    return merged

def mergesort(unsorted):
    if not unsorted or len(unsorted) < 2:
        return unsorted
    else:
        n = len(unsorted)
        mid = n//2
        left = mergesort(unsorted[:mid])
        right = mergesort(unsorted[mid:])
        merged = [None] * n
        return merge(merged, left, right)


def main():
    lo = 0
    hi = 100
    n = 10
    arr = [random.randint(lo, hi) for _ in range(n)]
    arr_sort = sorted(arr[:])
    assert mergesort(arr)==arr_sort

if __name__ == "__main__":
    main()

