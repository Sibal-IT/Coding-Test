import sys


def main():
    n = int(input())
    arr = list(list(map(int, input().split())) for _ in range(n))
    result = 0
    for i in arr:
        result = max(result, sum(i))
    for i in range(n):
        tmp_sum = 0
        for j in range(n):
            tmp_sum += arr[j][i]
        result = max(result, tmp_sum)
    tmp_sum = 0
    for i in range(n):
        tmp_sum += arr[i][i]
    result = max(result, tmp_sum)
    i = 0
    tmp_sum = 0
    for j in range(n - 1, -1, -1):
        tmp_sum += arr[i][j]
        i += 1
    result = max(result, tmp_sum)
    print(result)

if __name__ == "__main__":
    main()
