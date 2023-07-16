import sys


def kh_main():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0
    arr.sort(reverse=True)
    for i in range(len(arr) - 1):
        if arr[i] == m:
            cnt += 1
            continue
        for j in range(i + 2, len(arr) + 1):
            if sum(arr[i:j]) > m:
                break
            elif sum(arr[i:j]) == m:
                cnt += 1
                break
    print(cnt)


def main():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0
    lt = 0
    rt = 1
    tot = arr[0]
    while True:
        if tot < m:
            if rt < n:
                tot += arr[rt]
                rt += 1
            else:
                break
        elif tot == m:
            cnt += 1
            tot -= arr[lt]
            lt += 1
        else:
            tot -= arr[lt]
            lt += 1
    print(cnt)

if __name__ == "__main__":
    main()
