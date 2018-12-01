import random

def quicksort(arr):
    return None


def main():
    lo = 0
    hi = 100
    n = 10
    arr = [random.randint(lo, hi) for x in range(n)]
    print(arr)
    print(quicksort(arr))

if __name__ == "__main__":
    main()

