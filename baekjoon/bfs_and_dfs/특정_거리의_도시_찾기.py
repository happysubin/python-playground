import sys
from collections import deque

input = sys.stdin.readline

cities, roads, min_value, start = map(int, input().split())
visited = [False] * (cities + 1)
result = []

graph = [[] for _ in range(cities + 1)]

for _ in range(roads):
    node, node2 = map(int, input().split())
    graph[node].append(node2)

queue = deque()
queue.append((start, 0))
visited[start] = True

while queue:
    now, cnt = queue.popleft()

    if cnt == min_value:
        result.append(now)
    else:
        for nxt in graph[now]:
            if not visited[nxt]:
                visited[nxt] = True
                queue.append((nxt, cnt + 1))

if result:
    result.sort()
    sys.stdout.write("\n".join(map(str, result)) + "\n")
else:
    sys.stdout.write("-1\n")