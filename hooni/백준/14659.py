##한조 서열정리하고옴ㅋㅋ

import sys
input = sys.stdin.readline

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    a = 0
    cnt = 0
    result = list()
    for i in arr:
        if a > i:
            cnt += 1
        else:
            a=i
            result.append(cnt)
            cnt = 0
    result.append(cnt)        
    print(max(result))

if __name__ == "__main__":
    main()

