from sys import stdin

def main():
    input = stdin.readline

    # for BOJ
    n = int(input().strip())
    temp = [list(map(int, input().split())) for _ in range(n)]

    # for test
    # n = 11
    # temp = [[1, 4], [3, 5], [0, 6], [5, 7], [3, 8], [5, 9], [6, 10], [8, 11], [8, 12], [2, 13], [12, 14]]

    print(solution(n, temp))

def solution(n, rooms):
    # sorted 메소드 사용해서 정렬할 경우, key=lamda라고 입력해야 사용 가능
    # 두 개의 조건을 사용하고 싶을 때는 x: (괄호치고 조건 두 개 사용)
    rooms = sorted(rooms, key=lambda x: (x[1], x[0]))

    now = rooms[0]
    answer = 1
    
    for i in range(1, len(rooms)):
        
        # 이 부분에서 <=로 설정하는 것 역시 중요하다.
        if now[1] <= rooms[i][0]:
            answer += 1
            now = rooms[i]
            # print("now:", now)
            
    return answer

if __name__ == "__main__":
    main()