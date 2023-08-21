from sys import stdin

def solution(n, status, target):
    answer = 0

    # 1번 스위치를 처음부터 누르게 하면 실패함
    # 2번 누르고 1번 누르고 다시 돌아가도록 조치

    for i in range(n):
        if i == 0:
            i = 1
        elif i == 1:
            i = 0
        print("i 확인:", i, status[i] == target[i])

        if status[i] != target[i]:
            print("조건문 진입")
            answer += 1
            # print("중간 status 체크")
            # print(status[i-1:i+2])
            status[i-1:i+2] = map(lambda x: not x, status[i-1:i+2]) # i = 0일때 빈 리스트가 나옴...
            print(list(map(lambda x: not x, status[i-1:i+2])))
            print(status[0:2])
            

    print("\n최종 status:", status)
    if status == target:
        return answer

def main():
    input = stdin.readline
    n = int(input().strip())
    status = list(map(int, input().strip()))
    target = list(map(int, input().strip()))

    status = list(map(bool, status))
    target = list(map(bool, target))

    print(solution(n, status, target))

if __name__ == "__main__":
    main()


# 백준 질문 게시판 참조
# 맨 앞부터 상태를 하나씩 정하면서 최종 원하는 답과 비교하면서 끝까지 가다가 마지막 부분에서 답이 될수 있는지 없는지 보면 될것 같아요
# "1번 스위치를 누를 수 없다"라는 조건이 추가되면 비교적 간단하게 해결할 수 있습니다.
# 그 문제를 푼 다음, 1번 스위치를 한 번 누르고 같은 문제를 풀면 됩니다.

