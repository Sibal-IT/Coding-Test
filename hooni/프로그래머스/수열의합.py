## 수열의 합 - 프로그래머스

# 비내림차순으로 정렬된 수열이 주어질 때, 다음 조건을 만족하는 부분 수열을 찾으려고 합니다.

# 기존 수열에서 임의의 두 인덱스의 원소와 그 사이의 원소를 모두 포함하는 부분 수열이어야 합니다.
# 부분 수열의 합은 k입니다.
# 합이 k인 부분 수열이 여러 개인 경우 길이가 짧은 수열을 찾습니다.
# 길이가 짧은 수열이 여러 개인 경우 앞쪽(시작 인덱스가 작은)에 나오는 수열을 찾습니다.
# 수열을 나타내는 정수 배열 sequence와 부분 수열의 합을 나타내는 정수 k가 매개변수로 주어질 때, 위 조건을 만족하는 부분 수열의 시작 인덱스와 마지막 인덱스를 배열에 담아 return 하는 solution 함수를 완성해주세요. 이때 수열의 인덱스는 0부터 시작합니다.

#첫번째 시도
def solution(sequence, k):
    answer = [0, len(sequence)]
    sum_ = sequence[0]
    lt = 0
    rt = 1
    if sequence[-1] == k:
        return [len(sequence)-1, len(sequence)-1]
    for now in range(1, len(sequence)):
        rt = now
        if sequence[now] == k:
                return [now, now]
        if sum(sequence[lt:rt + 1]) == k:
            if (rt - lt) < (answer[1] - answer[0]):
                answer[0] = lt
                answer[1] = rt
        elif sum(sequence[lt:rt + 1]) > k:
            while lt < rt :
                if sum(sequence[lt:rt + 1]) == k:
                    if (rt - lt) < (answer[1] - answer[0]):
                        answer[0] = lt
                        answer[1] = rt
                        break
                lt = lt + 1
        
    return answer


#다시푼시도
def solution(sequence, k):
    answer = [0, len(sequence)]
    sum_ = 0
    lt = 0
    rt = -1
    while True :
        if sum_ < k:
            rt += 1
            if rt >= len(sequence):
                break
            sum_ += sequence[rt]
        else:
            sum_ -= sequence[lt]
            if lt >= len(sequence):
                break
            lt += 1
        if sum_ == k:
            if (rt - lt) < (answer[1] - answer[0]):
                answer[0] = lt
                answer[1] = rt
    return answer