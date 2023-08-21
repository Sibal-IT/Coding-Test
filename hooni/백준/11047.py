## 동전 0

import sys
input = sys.stdin.readline

def main():
    n, k = map(int, input().split())
    arr = list(int(input()) for _ in range(n))
    arr.sort(reverse=True)
    cnt = 0
    while(True):
        if k == 0:
            break
        else:
            for i in range(n):
                if k - arr[i] >= 0:
                    cnt = cnt + (k // arr[i])
                    k = k % arr[i]
                    break
    print(cnt)


if __name__ == "__main__":
    main()