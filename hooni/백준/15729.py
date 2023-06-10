import sys

input = sys.stdin.readline

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    result = [0 for _ in range(n)]
    cnt = 0
    for i in range(n):
        if arr[i] != result[i]:
            cnt += 1
            if result[i] == 1:
                result[i] = 0
            else :
                result[i] = 1
            if i + 1 < n:
                if result[i + 1] == 1:
                    result[i + 1] = 0
                else :
                    result[i + 1] = 1
            if i + 2 < n:
                if result[i + 2] == 1:
                    result[i + 2] = 0
                else :
                    result[i + 2] = 1
    print(cnt)

if __name__ == "__main__":
    main()