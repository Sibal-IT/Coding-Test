import sys


def main():
    arr_pil = input()
    arr1 = list(arr_pil[:])
    # print(arr1)
    n = int(input())
    arr = list(input() for i in range(n))
    result = list()
    t1 = 0
    for i in range(1, n + 1):
        t1 = 0
        for j in arr[i - 1]:
            if arr1[t1] == j:
                # print(t1)
                # print(arr1[t1])
                # print(j)
                t1 += 1
                if t1 == len(arr1):
                    break
        if t1 == len(arr1):
            result.append("#" + str(i) + " YES")
        else:
            result.append("#" + str(i) + " NO")
    for i in result:
        print(i)


if __name__ == "__main__":
    main()
