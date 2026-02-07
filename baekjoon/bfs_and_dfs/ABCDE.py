# n 은 사람 수 m은 친구 관계 수
n, m = map(int, input().split())

graph = [ [] for i in range(n)]

answer = False

def dfs(start, visited, depth):
    global answer
    if depth == 4:
        answer = True
        return 
    
    visited[start] = True
    
    for i in graph[start]:
        if not visited[i]:
            dfs(i, visited, depth + 1)
        
    # 경로 탐색이므로 되돌아오면 반드시 해제(backtracking) 해야 함        
    visited[start] = False

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)):
    visited = [False] * n
    dfs(i, visited, 0)
    if answer:
        break

if answer:
    print(1)
else:
    print(0)