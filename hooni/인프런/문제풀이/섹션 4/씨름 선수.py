import sys


def main():
    n = int(input())
    arr = list(list(map(int, input().split())) for _ in range(n))
    arr.sort(key=lambda x : (x[0], x[1]))
    cnt = 0
    for i in range(n):
        flag = True
        for j in range(i + 1, n):
            if arr[i][1] <= arr[j][1]:
                flag = False
                break
        if flag :
            cnt += 1
    print(cnt)


if __name__ == "__main__":
    main()
