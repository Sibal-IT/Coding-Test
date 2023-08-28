import sys


def main():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    cnt = 0
    i = 0
    while arr:
        if len(arr) > 1 and arr[0] + arr[-1] <= m:
            arr.pop(0)
            arr.pop()
            cnt += 1
        else:
            arr.pop()
            cnt += 1

    print(cnt)


if __name__ == "__main__":
    main()
