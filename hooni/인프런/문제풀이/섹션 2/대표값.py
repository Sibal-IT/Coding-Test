import sys

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    mid = round(sum(arr) / n)
    # print(mid)
    arr1 = list([0, 0] for _ in range(n))
    # print(arr1)
    for i in range(1, len(arr1) + 1):
        arr1[i - 1][0] = arr[i - 1] - mid
        arr1[i - 1][1] = i
    arr1.sort(key = lambda x : x[0])

    for i in arr1:
        if i[0] >= 0 :
            print("%d %d" %(mid, i[1]))
            break
        

if __name__ == "__main__":
    main()