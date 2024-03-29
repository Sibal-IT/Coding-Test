import sys


def main():
    k, n = map(int, input().split())
    arr = list(int(input()) for _ in range(k))
    arr.sort()
    lt = 1
    rt = arr[k - 1]
    result = list()
    while lt <= rt:
        mid = (lt + rt) // 2
        result_cnt = 0
        for i in arr:
            result_cnt += i // mid
            # print(i//mid)
        # if result_cnt == n:
        #     print(mid)
        #     return
        if result_cnt >= n:
            result.append(mid)
            lt = mid + 1
        else:
            rt = mid - 1
    print(max(result))


if __name__ == "__main__":
    main()
