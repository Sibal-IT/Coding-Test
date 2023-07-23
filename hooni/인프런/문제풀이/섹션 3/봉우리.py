import sys


def main():
    n = int(input())
    arr = list([0 for _ in range(n + 2)] for _ in range(n + 2))
    for i in range(1, n + 1):
        arr_tmp = list(map(int, input().split()))
        for j in range(n):
            arr[i][j + 1] = arr_tmp[j]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    cnt = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            flag = True
            for k in range(0, 4):
                if arr[i][j] <= arr[i - dx[k]][j - dy[k]]:
                    flag = False
                    break
            if flag:
                # print(arr[i][j])
                cnt += 1
    print(cnt)
    


if __name__ == "__main__":
    main()
