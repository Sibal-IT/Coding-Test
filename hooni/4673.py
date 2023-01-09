##셀프 넘버

import sys
input = sys.stdin.readline

def main():
    arr = [i for i in range(10002)]
    for i in range(10001):
        dn = i
        tempi = str(i)
        for j in tempi[:]:
            dn += int(j)
        if dn <= 10000:
            arr[dn] = 0

    for i in arr[:10001]:
        if i != 0:
            print(i)

if __name__ == "__main__":
    main()

    