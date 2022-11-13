# 서로 다른 N개의 자연수의 합이 S라고 한다. S를 알 때, 자연수 N의 최댓값은 얼마일까?
# 시간은 그냥 input 사용이 아주 약간 더 빠름
#import sys
# s = int(sys.stdin.readline().strip())

s = int(input())
tot = 0
answer = 0

if s == 1:
    answer = 1
else: 
    for i in range(1, s):
        # print('i:', i)
        if tot + i == s:
            answer = i
            break
        elif tot + i > s:
            break
        else:
            tot += i
            answer = i

print(answer)