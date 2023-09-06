import sys


def main():
    n, m = map(int, input().split())
    num = list(map(int, str(n)))
    result = list()
    for i in num:
        while result and m > 0 and result[-1] < i:
            result.pop()
            m -= 1
        result.append(i)
    if m != 0:
        result = result[:-m]

    for i in result:
        print(i, end='')


if __name__ == "__main__":
    main()
