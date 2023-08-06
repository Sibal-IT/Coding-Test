import sys


def main():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    lt = 1
    rt = sum(arr)
    result = list()
    while lt <= rt:
        mid = (lt + rt) // 2
        cnt = 1
        tmp = 0
        for i in arr:
            # tmp += i
            if tmp + i > mid:
                # print(tmp + i, mid)
                tmp = i
                cnt += 1
            else :
                tmp += i
        if cnt <= m:
            result.append(mid)
            rt = mid - 1
        else:
            lt = mid + 1
    # print(result)
    print(min(result))

if __name__ == "__main__":
    main()
