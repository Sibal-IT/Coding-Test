import sys

def count_gam(arr, n):
    app_sum = 0
    lt = 0
    rt = n - 1
    for i in range(n//2 + 1):
        for j in range(lt, rt + 1):
            app_sum += arr[i][j]
        lt += 1
        rt -= 1
    lt -= 1
    rt += 1
    for i in range(n//2 + 1, n):
        lt -= 1
        rt += 1
        for j in range(lt, rt + 1):
            app_sum += arr[i][j]
    return app_sum

def rotate_right(arr, n):
    if not arr:
        return arr
    n %= len(arr)
    if not n:
        return arr
    left = arr[:-n]
    right = arr[-n:]  
    return right + left

def rotate_left(arr, n):
    if not arr:
        return arr
    n %= len(arr)
    if not n:
        return arr
    left = arr[:n]
    right = arr[n:]  
    return right + left

def main():
    n = int(input())
    arr = list(list(map(int, input().split())) for _ in range(n))
    m = int(input())
    arr_rot = list(list(map(int, input().split())) for _ in range(m))
    for i in arr_rot:
        if i[1] == 0:
            lt = i[0] - 1
            arr[lt] = rotate_left(arr[lt], i[2])        
        else:
            lt = i[0] - 1
            arr[lt] = rotate_right(arr[lt], i[2])
    # print(arr)
    print(count_gam(arr, n))

if __name__ == "__main__":
    main()
