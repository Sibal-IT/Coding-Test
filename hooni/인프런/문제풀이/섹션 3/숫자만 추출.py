import sys

def main():
    tmp_str = input()
    arr_str = list(tmp_str[:])
    str_int = ""
    for i in arr_str:
        if "0" <= i <= "9":
            str_int += i
    print(int(str_int))
    cnt = 0
    for i in range(1, int(str_int) + 1):
        if int(str_int) % i == 0:
            cnt += 1
    print(cnt)
    

if __name__ == "__main__":
    main()