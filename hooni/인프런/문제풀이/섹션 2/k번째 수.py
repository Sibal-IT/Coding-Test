import sys

def main():
    t = int(input())
    result = list()
    for _ in range(t):
        n, s, e, k = map(int, input().split())
        arr = list(map(int, input().split()))
        arr1 = list(arr[s - 1: e])
        arr1.sort()
        result.append(arr1[k - 1])
    
    for i in range(1, len(result) + 1):
        print("#%d %d" %(i, result[i - 1]))

if __name__ == "__main__":
    main()