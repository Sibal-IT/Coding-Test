import sys


def main():
    n, m = map(int, input().split())
    arr = list(int(input()) for _ in range(n))
    arr.sort()
    lt = 0
    rt = arr[n - 1]
    res = 0
    while lt <= rt:
        mid = (lt + rt) // 2
        cnt = 1
        ep = arr[0]
        for i in range(1, n):
            if arr[i] - ep >= mid:
                cnt += 1
                ep = arr[i]
        if cnt < m:
            rt = mid - 1
        else:
            res = mid
            lt = mid + 1
    print(res)


if __name__ == "__main__":
    main()
