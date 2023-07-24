import sys


def main():
    arr = list(list(map(int, input().split())) for _ in range(9))
    flag = True
    for i in range(9):
        ch1 = [0 for _ in range(10)]
        ch2 = [0 for _ in range(10)]
        for j in range(9):
            ch1[arr[i][j]] = 1
            ch2[arr[j][i]] = 1
        if sum(ch1) != 9 or sum(ch2) != 9:
            flag = False
    for i in range(0, 3, 6):
        for j in range(0, 3, 6):
            ch1 = [0 for _ in range(10)]
            for dx in range(3):
                for dy in range(3):
                    ch1[arr[i + dx][j + dy]] = 1
            if sum(ch1) != 9:
                flag = False
    if flag:
        print("YES")
    else:
        print("NO")            
    

            
            
    

if __name__ == "__main__":
    main()
