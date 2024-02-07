from collections import deque

# 구현했으나 백준 채점 시 메모리 초과
# 메모리 따위는 신경쓰지 않는 코딩 이슈
# 정답 참조 - bfs 사용할 것.
def bfs(z):
    q = deque([(z, 1)])

    while q:
        x, count = q.popleft()

        if x == b:
            return count
        
        for i in (x*2, int(str(x) + '1')):
            if 0 <= i <= b:
                q.append((i, count + 1))
        
    return -1

a, b = list(map(int, input().split()))
print(bfs(a))

