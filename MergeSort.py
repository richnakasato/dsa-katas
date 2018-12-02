import random

def mergesort():
    pass


def main():
    lo = 0
    hi = 100
    n = 10
    arr = [random.randint(lo, hi) for _ in range(n)]
    arr_sort = sorted(arr[:])
    assert mergesort()==arr_sort

if __name__ == "__main__":
    main()

