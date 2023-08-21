import sys

input = sys.stdin.readline

def main():
    n = int(input())
    a_1 = int(input())
    a = [int(input()) for _ in range(n - 1)]
    a.sort(reverse=True)
    cnt = 0
    if n == 1:
        print(0)
        return
    else:
        while a[0] >= a_1:
            a[0] -= 1
            a_1 += 1
            cnt += 1
            a.sort(reverse=True)
    print(cnt)

if __name__ == "__main__":
    main()