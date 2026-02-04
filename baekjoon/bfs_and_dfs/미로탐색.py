from collections import deque

n, m = map(int, input().split())
graph = []
visited = []

for _ in range(n):
    row = list(map(int, input()))
    vrow = [False] * (m)
    graph.append(row)
    visited.append(vrow)

# 1,1 d에서 출발. 최소이므로 bfs

def bfs(): 
    answer = 0
    queue = deque()
    queue.append([0, 0, 1])
    visited[0][0] = True
    while queue:
        a, r, d = queue.popleft()
        
        if a == n -1 and r == m -1:
            print(d)
            break
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            tx = a + dx
            ty = r + dy
            if tx >= 0 and tx < n and ty >= 0 and ty < m:
                if not visited[tx][ty] and graph[tx][ty] == 1:
                    queue.append([tx, ty, d + 1])
                    visited[tx][ty] = True
bfs()
