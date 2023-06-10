import sys

def main(): 
    n, k = map(int, input().split())
    cnt = 0
    flag = 0
    for i in range(1, n + 1):
        if n % i == 0:
            cnt += 1
        if cnt == k :
            print(i)
            flag = 1
            break

    if flag == 0:
        print(-1)

if __name__ == '__main__':
    main()