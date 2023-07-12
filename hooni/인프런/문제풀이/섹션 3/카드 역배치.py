import sys


def main():
    arr = list(x for x in range(21))
    for _ in range(10):
        a, b = map(int, input().split())
        tmp_arr = list(reversed(arr[a:b + 1]))
        cnt = 0
        for i in range(a, b + 1):
            arr[i] = tmp_arr[cnt]
            cnt += 1
    for i in arr[1:]:
        print(i, end=' ')


if __name__ == "__main__":
    main()
