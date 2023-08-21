import sys


def main():
    n = int(input())
    arr1 = list(map(int, input().split()))
    result = list(0 for _ in range(n))
    for i in range(len(arr1)):
        if i == 0:
            if arr1[i] == 1:
                result[i] = 1
        else:
            if arr1[i] == 1:
                if result[i - 1] >= 1:
                    result[i] = result[i - 1] + 1
                else:
                    result[i] = 1
    print(sum(result))


if __name__ == "__main__":
    main()
