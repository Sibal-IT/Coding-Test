import sys

def main():
    n = int(input())
    arr = list(True for _ in range(n + 2))
    if n == 1:
        print(0)
    for i in range(2, n + 1):
        if arr[i]:
            j = i * 2
            cnt_i = 2
            while j <= n + 1:
                arr[j] = False
                cnt_i += 1
                j = i * cnt_i
    cnt = 0
    for i in range(2, n + 1):
        if arr[i]:
            cnt += 1
    print(cnt)
    

if __name__ == '__main__':
    main()