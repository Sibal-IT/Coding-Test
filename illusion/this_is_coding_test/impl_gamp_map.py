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

# 보조 함수
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

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

print(count)