import sys
from itertools import combinations


def main():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr1 = list(combinations(arr, 3))
    arr1.sort(key=lambda x: sum(x), reverse=True)
    sum1 = 0
    cnt = 0
    for i in arr1:
        if sum1 != sum(i):
            cnt += 1
            sum1 = sum(i)
        if k == cnt:
            print(sum(i))
            break


if __name__ == "__main__":
    main()
