import sys


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    result = list()
    if arr[0] > arr[-1]:
        prev = arr[0]
        arr.pop(0)
    elif arr[0] < arr[-1]:   
    while arr:
        if len(arr) == 2:
            if prev
            break
        if len(arr) > 1 and arr[0] + arr[-1] <= m:
            arr.pop(0)
            arr.pop()
            cnt += 1
        else:
            arr.pop()
            cnt += 1

    print(len(result))
    for i in result:
        print(i, end=' ')


if __name__ == "__main__":
    main()
