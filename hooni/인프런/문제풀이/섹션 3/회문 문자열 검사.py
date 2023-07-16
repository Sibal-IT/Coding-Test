import sys

def main():
    n = int(input())
    result = list()
    for j in range(n):
        flag = 0
        arr_str = input()
        arr_str = arr_str.upper()
        arr = list(arr_str[:])
        for i in range(len(arr) // 2):
            if arr[i] != arr[len(arr) - 1 - i]:
                flag = 1
                str_tp = "#" + str(j + 1) + " NO"
                result.append(str_tp)
                break
        if flag == 0:
            str_tp = "#" + str(j + 1) + " YES"
            result.append(str_tp)
    for i in result:
        print(i)

if __name__ == "__main__":
    main()