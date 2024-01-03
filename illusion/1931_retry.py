from sys import stdin

def main():

    # for BOJ
    # input = stdin.readline
    # n = int(input().strip())
    # temp = [list(map(int, input().split())) for _ in range(n)]

    # for test
    n = 11
    temp = [[1, 4], [3, 5], [0, 6], [5, 7], [3, 8], [5, 9], [6, 10], [8, 11], [8, 12], [2, 13], [12, 14]]

    print(solution(n, temp))

def solution(n, rooms):
    answer = 0
   
    rooms = sorted(rooms, key=lambda x: (x[1], x[0]))

    now = rooms[0]
    answer += 1

    for i in range(1, len(rooms)):
        if now[1] <= rooms[i][0]:
            answer += 1
            now = rooms[i]

    return answer

if __name__ == "__main__":
    main()