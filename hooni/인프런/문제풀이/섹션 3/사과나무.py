import sys


def main():
    n = int(input())
    arr = list(list(map(int, input().split())) for _ in range(n))
    app_sum = 0
    lt = n // 2
    rt = n // 2
    for i in range(n//2 + 1):
        for j in range(lt, rt + 1):
            app_sum += arr[i][j]
        lt -= 1
        rt += 1
    lt += 1
    rt -= 1
    for i in range(n//2 + 1, n):
        lt += 1
        rt -= 1
        for j in range(lt, rt + 1):
            app_sum += arr[i][j]
        
    print(app_sum)
    

if __name__ == "__main__":
    main()
