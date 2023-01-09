##전구와 스위치

import sys
import copy
# input = sys.stdin.readline

def main():
    n = int(input())
    a = list(map(int, input()))
    b = list(map(int, input()))
    # 1번 전구를 안눌렀을 때의 상태
    temp1 = copy.deepcopy(a)
    # 1번 전구를 눌렀을 때의 상태
    temp2 = copy.deepcopy(a)
    temp2[0] = 1 - temp2[0]
    temp2[1] = 1 - temp2[1]
    answer = sys.maxsize
    cnt = 0
    flag = False
    for i in range(1, n):
        if temp1[i-1] != b[i-1]:
            cnt += 1
            for j in range(i-1, i+2):
                if j < n:
                    temp1[j] = 1 - temp1[j]
        if temp1 == b :
            flag = True
            if answer > cnt :
                answer = cnt
    cnt = 1
    for i in range(1, n):
        if temp2[i-1] != b[i-1]:
            cnt += 1
            for j in range(i-1, i+2):
                if j < n:
                    temp2[j] = 1 - temp2[j]
        if temp2 == b :
            flag = True
            if answer > cnt :
                answer = cnt

    if flag:
        print(answer)
    else:
        print(-1)


if __name__ == "__main__":
    main()