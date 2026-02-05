
total = int(input())
pair = int(input())

visited = [False  for _ in range(total + 1)]
answer = 0 

def dfs(now, graph):
    global answer 

    if visited[now]:
        return
    visited[now] = True
    answer += 1
    for i in graph[now]:
        if not visited[i]:
            dfs(i, graph)


graph = [[] for _ in range(total + 1)]

for _ in range(pair):
    f, s = map(int, input().split())
    graph[f].append(s)
    graph[s].append(f)

dfs(1, graph)
print(answer - 1)