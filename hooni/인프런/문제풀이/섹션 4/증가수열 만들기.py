import sys


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    prev = 999999999
    result = ''
    lt = 0
    rt = n - 1
    last = 0
    tmp = list()
    while lt <= rt:
        if last < arr[lt]:
            tmp.append((arr[lt], 'L'))
        if last < arr[rt]:
            tmp.append((arr[rt], 'R'))
        tmp.sort(key=lambda x:x[0])
        if len(tmp) == 0:
            break
        else:
            result = result+tmp[0][1]
            last = tmp[0][0]
            if tmp[0][1] == 'L':
                lt = lt+1
            else:
                rt = rt-1
        tmp.clear()

    print(len(result))
    print(result)
    # for i in result:
    #     print(i, end=' ')


if __name__ == "__main__":
    main()
