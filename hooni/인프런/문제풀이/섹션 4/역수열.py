import sys


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    arr = arr[::-1]
    result = []
    
    for i in arr:
        result.insert(i, n)
        n -= 1

    for i in result:
        print(i, end=' ')
    # print(result)


if __name__ == "__main__":
    main()
