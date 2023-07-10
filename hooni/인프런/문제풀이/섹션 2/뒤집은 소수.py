import sys

def reverse(x):
    tp_x = str(x)
    int_x = ''
    for i in tp_x[::-1]:
        int_x += i
    return int(int_x)

def isPrime(x):
    if x == 1:
        return False
    arr = list(True for _ in range(x + 2))
    for i in range(2, x + 1):
        if arr[i]:
            j = i * 2
            cnt_i = 2
            while j <= x + 1:
                arr[j] = False
                cnt_i += 1
                j = i * cnt_i
    if arr[x]:
        return True
    else:
        return False

def main():
    result = list()
    n = int(input())
    arr1 = list(map(int, input().split()))

    for i in range(len(arr1)):
        arr1[i] = reverse(arr1[i])
    for i in arr1:
        if isPrime(i):
            result.append(i)
    for i in result:
        print(i, end=' ')
    

if __name__ == '__main__':
    main()