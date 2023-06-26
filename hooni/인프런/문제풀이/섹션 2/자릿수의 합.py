import sys

def digit_sum(x):
    t = list(str(x))
    t_sum = 0
    for i in t:
        t_sum += int(i)
    return t_sum

def main():
    n = int(input())
    arr = map(int, input().split())
    result = list()

    for i in arr:
        result.append([i, digit_sum(i)])

    result.sort(key=lambda x : x[1], reverse=True)
    print(result[0][0])

if __name__ == '__main__':
    main()
