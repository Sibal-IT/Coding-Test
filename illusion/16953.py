import math

problem = '''
문제: 정수 A를 B로 바꾸려고 한다. 가능한 연산은 다음과 같은 두 가지이다.

2를 곱한다.
1을 수의 가장 오른쪽에 추가한다. 
A를 B로 바꾸는데 필요한 연산의 최솟값을 구해보자.

[ 2,  4,  8,  16, 32, 64, 128, 256]
[21, 42, 84, 168, ...]
[    41, 82, 164, ...]
[        81, 162]

[ 4,  8,  16, 32, 64, 128, ...]
[41, 82, 164, ...]
[    81, 162, ...]
[        161, ...]

[100,   200,  400,  800, 16000, 32000, 64000, ...]
[1001, 2002, 4004, 8008, 16016, 32032, 64064, ...]
[      2001,|4002|,8004, 16008, 32016, 64032, ...]
[            4001, 8002, 16004, 32008, 64016, ...]

-> 만약 숫자 뒤에 1이 붙을 경우, 1을 제거하고 가장 빠른 숫자를 찾아 단계 찾기
-> 리스트를 만들 때, 2씩 곱하는 1행 / 2 만큼 열을 만들면 된다.

=> 답은 BFS로 풀어야 했음. 내 방식대로 풀면 메모리 초과 발생
'''

def solution(a, b):
    answer = -1
    temp = a

    for i in range(b // a): 
        if temp > b:
            temp = i
            break
        else:
            temp *= 2
    
    print('temp: ', temp)
    
    # temp는 행 길이
    # temp / 2는 열 길이
    
    graph = [[0] * temp for _ in range(math.ceil(temp / 2))]

    for i in range(len(graph)):
        # 각 행의 0번 값을 넣어줌
        if i == 0:
            graph[0][0] = a
        else: 
            calc2 = int(str(graph[0][i-1]) + '1')
            print('calc2: ', calc2)
            if calc2 == b:
                return i + j
            else:
                graph[i][0] = calc2
        
        for j in range(1, len(graph[i])):
            print('i:', i, ' j:', j)
            # debug
            for g in graph:
                print(g)
            print('------')

            calc = graph[i][j-1] * 2
            print(calc, b)

            if int(calc) == int(b):
                print('i+j')
                return i + j + 1
            elif int(str(calc) + '1') == b:
                print('i+j+1')
                return i + j + 2
            else:
                graph[i][j] = calc

    return answer


# 2 162
# 4 42
# 100 40021
# A, B = map(int, input().split())
# A, B = 2, 162
# A, B = 4, 42
A, B = 100, 40021

print(solution(A, B))