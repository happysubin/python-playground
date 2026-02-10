from collections import deque

n, m, k = map(int, input().split())

graph = [[0] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]

answer = 0

for i in range(k):
    x, y = map(int, input().split())
    graph[x - 1][y - 1] = 1



def bfs(start_x, start_y):
    answer = 1
    visited[start_x][start_y] = True
    queue = deque()
    queue.append((start_x, start_y))
    while queue:
        next_x, next_y = queue.popleft()
        for nx, ny in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            rx = nx + next_x
            ry = ny + next_y
            if rx >= 0 and rx < n and ry >= 0 and ry < m:
                if not visited[rx][ry] and graph[rx][ry] == 1: 
                    visited[rx][ry] = True
                    queue.append((rx, ry))
                    answer += 1
    return answer

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            answer = max(answer, bfs(i, j))

print(answer)
