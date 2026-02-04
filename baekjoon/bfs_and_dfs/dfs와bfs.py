from collections import deque

# n은 정점의 개수, M은 간선의 개수, V는 노드의 개수
n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]

# 인접 리스트
for i in range(m):
    u, w = map(int, input().split())
    graph[u].append(w)
    graph[w].append(u)

for edge in graph:
    edge.sort()

dfs_visited = [False] * (n + 1)

def dfs(start):
    dfs_visited[start] = True
    print(start, end=' ')
    for next_node in graph[start]:
        if not dfs_visited[next_node]:
            dfs(next_node)

def bfs(start):
    visited = [False] * (n + 1)
    queue = deque()
    visited[start] = True
    queue.append(start)
    while queue:
        node = queue.popleft()
        print(node, end=' ')

        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)


dfs(v)
print("")
bfs(v)
