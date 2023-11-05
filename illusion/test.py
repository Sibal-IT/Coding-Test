from collections import deque

# 인접 리스트로 그래프를 표현합니다.
graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 6, 7],
    4: [2],
    5: [2, 8],
    6: [3],
    7: [3],
    8: [5]
}

def bfs(graph, start_node):
    visited = []  # 방문한 노드를 저장하는 리스트
    queue = deque()  # BFS 탐색을 위한 큐
    queue.append(start_node)  # 시작 노드를 큐에 추가

    while queue:  # 큐가 비어있지 않은 동안
        node = queue.popleft()  # 큐의 맨 앞 노드를 꺼내옴
        if node not in visited:  # 방문하지 않은 노드일 경우
            visited.append(node)  # 방문한 노드 리스트에 추가
            queue.extend(graph[node])  # 해당 노드의 인접 노드를 큐에 추가

    return visited

print(bfs(graph, 1))  # [1, 2, 3, 4, 5, 6, 7, 8]