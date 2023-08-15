import sys


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())
    for i in range(m):
        arr.sort()
        # if arr[0] > arr[1]:
        #     tmp = arr[0]
        #     arr[0] = arr[1]
        #     arr[1] = tmp
        # if arr[-1] < arr[-2]:
        #     tmp = arr[-1]
        #     arr[-1] = arr[-2]
        #     arr[-2] = tmp
        arr[-1] -= 1
        arr[0] += 1
    # print(arr)
    print(max(arr) - min(arr))


if __name__ == "__main__":
    main()
