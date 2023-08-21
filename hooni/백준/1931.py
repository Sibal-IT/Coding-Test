import sys

input = sys.stdin.readline

def main():
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr.sort(key = lambda x : x[0])
    arr.sort(key = lambda x : x[1])
    # print(arr)
    cnt = 1
    f_t = arr[0][1]
    for i in range(1, len(arr)):
        if f_t <= arr[i][0]:
            f_t = arr[i][1]
            cnt += 1 
    print(cnt)

if __name__ == "__main__":
    main()
