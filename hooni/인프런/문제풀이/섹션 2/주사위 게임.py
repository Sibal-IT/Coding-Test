import sys


def main():
    n = int(input())
    result = 0
    for _ in range(n):
        arr = list(map(int, input().split()))
        arr.sort(reverse=True)
        if arr[0] == arr[1]:
            if arr[1] == arr[2]:
                result = max(result, 10000 + (arr[0]*1000))
            else:
                result = max(result, 1000 + (arr[0]*100))
        else:
            if arr[1] == arr[2]:
                result = max(result, 1000 + (arr[1]*100))
            else:
                result = max(result, arr[0]*100)
    print(result)


if __name__ == "__main__":
    main()
