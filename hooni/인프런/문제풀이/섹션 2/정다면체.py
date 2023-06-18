import sys

from itertools import product

def main():
    n, m = map(int, input().split())
    arr1 = list(i for i in range(1, n + 1))
    arr2 = list(i for i in range(1, m + 1))
    dict1 = dict()
    for i in arr1 :
        for j in arr2 :
            dict1[i + j] = dict1.get(i + j, 0) + 1
    sort_dict = sorted(dict1.items(), key = lambda x : x[1], reverse=True)

    t = sort_dict[0][1]
    result = list()
    for i in sort_dict:
        if i[1] == t:
            result.append(i[0])
            t = i[1]
        else :
            break

    for i in result:
        print(i, end=" ")


if __name__ == "__main__":
    main()