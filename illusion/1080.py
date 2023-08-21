from sys import stdin

def solution(N, M, A, B):
    answer = 0
    temp = []

    for i in range(N-2):
        # print('debug i:', i)
        for j in range(M-2):
            # print('debug j:', j)

            # 만약 다르면 뒤집기 시작
            if A[i][j] != B[i][j]:
                # print('조건문 진입')
                for k in range(i, i+3):
                    for l in range(j, j+3):
                        if A[k][l] == 1:
                            A[k][l] = 0
                        else:
                            A[k][l] = 1
                    # print(A)
                temp.append([i, j, i+3, j+3])
                answer += 1

    if A == B:
        return answer
    else:
        return -1


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    a, b = [], []

    for _ in range(n):
        a.append(list(map(int, input().strip())))
    for _ in range(n):
        b.append(list(map(int, input().strip())))

    if a == b:
        print(0)
    else:
        print(solution(n, m, a, b))

if __name__ == "__main__":
    main()