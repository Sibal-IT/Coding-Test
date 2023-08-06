import sys


def main():
    n, m = map(int, input().split())
    arr = list(int(input()) for _ in range(n))
    arr.sort()
    lt = 0
    rt = n
    while lt <= rt:
        mid = (lt + rt) // 2
        flag = False
        while True:
            if flag:
                break
            for i in range(1, n):
                if
    
   


if __name__ == "__main__":
    main()
