import random

def merge(arr, lhs, rhs):
    i = j = k = 0
    while i < len(lhs) and j < len(rhs):
        if lhs[i] < rhs[j]:
            arr[k] = lhs[i]
            i+=1
        else:
            arr[k] = rhs[j]
            j+=1
        k+=1
    while i < len(lhs):
        arr[k] = lhs[i]
        i+=1
        k+=1
    while j < len(rhs):
        arr[k] = rhs[j]
        j+=1
        k+=1
    return arr

def mergesort(arr):
    if len(arr) < 2:
        return arr
    else:
        res = [None] * len(arr)
        mid = len(arr)//2
        merge(res, mergesort(arr[mid:]), mergesort(arr[:mid]))
        return res


def main():
    lo = 0
    hi = 100
    n = 10
    arr = [random.randint(lo, hi) for x in range(n)]
    print(arr)
    print(mergesort(arr))

if __name__ == "__main__":
    main()

