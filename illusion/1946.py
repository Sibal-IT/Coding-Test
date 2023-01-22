# 백준 들어가보니 풀었던 문제
# 풀이 다시 참조 https://velog.io/@ledcost/백준-1946-파이썬-신입-사원-실버1-그리디

from sys import stdin

input = stdin.readline

def solution(new_face):
    new_face.sort()
    result = 1
    top = new_face[0][1]

    for i in range(1, len(new_face)):
        if new_face[i][1] < top:
            top = new_face[i][1]
            result += 1

    return result
    
    # 결과 오류 발생
    # for i in range(1, len(new_face)):
    #     for j in range(i, len(new_face)):
    #         if new_face[i][1] < new_face[j][1]:
    #             result += 1
    #             break

    # return 'result: ', result

n = int(input().strip())

for i in range(n):
    temp_list = []
    m = int(input().strip())
    for j in range(m):
        temp_list.append(list(map(int, input().strip().split())))

    print(solution(temp_list))

# 풀이용 각주
#[[1, 4], 
# [2, 3], 
# [3, 2], 
# [4, 1], 
# [5, 5]]

#[[1, 4], 
# [2, 5], 
# [3, 6], 
# [4, 2], 
# [5, 7], 
# [6, 1], 
# [7, 3]]