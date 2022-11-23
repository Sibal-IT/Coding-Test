# 30의 배수는 3의 배수이면서 10의 배수이기도 해야한다.
# 10의 배수가 되기 위해선 마지막 일의자리가 반드시 0으로 끝나야 하므로 입력값에 0이 없다면
# 30의 배수가 될 수 없기 때문에 바로 -1을 출력해주면 된다.
# 3의 배수가 되기 위해선 각 자리수의 합이 3의 배수이면 3의 배수이다.

def solution(n):
    flag = False

    n_list = []

    for i in n:
        if i == '0':
            flag = True
        n_list.append(int(i))
    
    if flag is False:
        return -1
    else:
        if sum(n_list) % 3 == 0:
            return ''.join(sorted(n, reverse=True))
        else:
            return -1

n = input()
print(solution(n))