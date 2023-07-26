import sys

def main():
    arr = list(list(map(int, input().split())) for _ in range(7))
    result = 0
    for i in range(7):
        for j in range(3):
            if arr[i][j] == arr[i][j + 4] and arr[i][j + 1] == arr[i][j + 3]:
                # print(i , j)
                result += 1
    for i in range(3):
        for j in range(7):
            if arr[i][j] == arr[i + 4][j] and arr[i + 1][j] == arr[i + 3][j]:
                # print(i, j)
                result += 1
    print(result)


if __name__ == "__main__":
    main()
