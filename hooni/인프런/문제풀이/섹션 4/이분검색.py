import sys


def main():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    lt = 0
    rt = n - 1
    while lt <= rt:
        mid = (lt + rt) // 2    
        if arr[mid] == m:
            break
        if  arr[mid] < m:
            lt = mid + 1
        else :
            rt = mid - 1

    print(mid + 1)


if __name__ == "__main__":
    main()
