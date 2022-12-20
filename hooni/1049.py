##기타줄

import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(m)]
    result = 0
    if n <= 6:
        arr.sort(key=lambda x:x[0])
        min1 = arr[0][0]
        arr.sort(key=lambda x:x[1])
        min2 = arr[0][1]*n
        if min1 < min2:
            print(min1)
        else:
            print(min2)
    else:
        arr.sort(key=lambda x:x[0])
        min1 = arr[0][0]
        arr.sort(key=lambda x:x[1])
        min2 = arr[0][1]
        if min1 < min2 * 6:
            cnt = n // 6
            result += cnt * min1
            cnt = n % 6
            if min1 > cnt * min2:
                result += cnt * min2
            else:
                result += min1
            print(result)
        else:
            print(n * min2)

if __name__ == "__main__":
    main()