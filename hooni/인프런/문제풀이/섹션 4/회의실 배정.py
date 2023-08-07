import sys


def main():
    n = int(input())
    arr = list(list(map(int, input().split())) for _ in range(n))
    arr.sort(key=lambda x: (x[1], x[0]))
    ep = arr[0][1]
    cnt = 1
    for i in range(1, n):
        if arr[i][0] >= ep:
            cnt += 1
            ep = arr[i][1]
    print(cnt)


if __name__ == "__main__":
    main()
