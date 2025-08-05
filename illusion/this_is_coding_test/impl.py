from sys import stdin

def wsad():
    
    n = int(stdin.readline())
    control = list(map(str, input().split()))

    location = [1, 1] #x, y

    for c in control:
        if c == 'L':
            if location[1] > 1:
                location[1] -= 1
        elif c == 'R':
            if location[1] < n:
                location[1] += 1
        elif c == 'U':
            if location[0] > 1:
                location[0] -= 1
        elif c == 'D':
            if location[0] < n:
                location[0] += 1

    return location

def wsad_answer():

    n = int(input())
    x, y = 1, 1
    plans = input().split()

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    move_types = ['L', 'R', 'U', 'D']

    for plan in plans:
        for i in range(len(move_types)):
            if plan == move_types[i]:
                nx = x + dx[i]
                ny = y + dy[i]
        
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
        
        x, y = nx, ny
    
    return x, y


def clock_is_ticking():

    result = 0

    hh = int(stdin.readline())

    for h in range(hh + 1):
        for m in range(60):
            for s in range(60):
                if '3' in str(h) + str(m) + str(s):
                    print(f'hour: {h}, min: {m}, sec: {s}')
                    result += 1


    return result


def chess():

    result = 0

    location = list(map(str, input()))

    x_dict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
    x = x_dict[location[0]]
    y = int(location[1])

    dx = [2,  2,  1,  1, -1, -1, -2, -2]
    dy = [1, -1,  2, -2,  2, -2,  1, -1]

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 1 or ny < 1 or nx > 8 or ny > 8:
            continue
        else:
            result += 1

    return result


# 보조 함수
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

def game_dev():

    # n, m = map(int, input().split())
    # a, b, d = map(int, input().split())

    # game_map = []
    # for _ in range(n):
    #     game_map.append(list(map(int, input().split())))
    n, m = 4, 4
    x, y, direction = 1, 1, 0

    game_map = [[1, 1, 1, 1], 
                [1, 0, 0, 1], 
                [1, 1, 0, 1], 
                [1, 1, 1, 1]]
    
    d = [[0] * m for _ in range(n)]
    d[x][y] = 1 # 방문처리

    # 북 동 남 서
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    count = 1
    turn_time = 0

    while True:
        turn_left()

        nx = x + dx[direction]
        ny = y + dy[direction]

        if d[nx][ny] == 0 and game_map[nx][ny] == 0:
            d[nx][ny] = 1
            x = nx
            y = ny
            count += 1
            turn_time = 0
            continue
        else:
            turn_time += 1
        
        if turn_time == 4:
            nx = x - dx[direction]
            ny = y - dy[direction]

            if game_map[nx][ny] == 0:
                x = nx
                y = ny
            else:
                break
            turn_time = 0
    
    return count




# print(wsad())
# print(wsad_answer())
# print(clock_is_ticking())
# print(chess())
print(game_dev())