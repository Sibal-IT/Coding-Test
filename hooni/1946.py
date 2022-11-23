import sys

input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = [list(map(int, input().split())) for _ in range(n)]
        a.sort(key = lambda x : x[0])
        cnt = 1
        a_2 = a[0][1]
        for i in range(len(a)):
            if a[i][1] < a_2:
                cnt += 1
                a_2 = a[i][1]
        print(cnt)

if __name__ == "__main__":
    main()