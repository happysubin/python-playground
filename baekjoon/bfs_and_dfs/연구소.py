from collections import deque

x, y = map(int, input().split())

graph = []
answer = 0 

for _ in range(x):
    graph.append(list(map(int, input().split())))


# 빈 칸 좌표를 미리 저장
empties = [(i, j) for i in range(x) for j in range(y) if graph[i][j] == 0]

# 1. 벽을 3개 짓는 모든 경우를 수행
def dfs(cnt, start):
    global answer

    # 3개 이상 벽을 못세운다.
    if cnt == 3:
        answer = max(answer, bfs())
        return

    for k in range(start, len(empties)):
        i, j = empties[k]
        graph[i][j] = 1
        dfs(cnt + 1, k + 1)
        graph[i][j] = 0    

def bfs() -> int:  
    visited = [[False] * y for _ in range(x)]
    queue = deque()
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == 2:
                visited[i][j] = True
                queue.append((i, j))

    while(queue):
        pop_x, pop_y = queue.popleft()

        for mx, my in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            target_x = mx + pop_x
            target_y = my + pop_y
            if(target_x >= 0 and target_x < x and target_y >= 0 and target_y < y):
                if not visited[target_x][target_y] and graph[target_x][target_y] == 0:
                    visited[target_x][target_y] = True
                    queue.append((target_x, target_y))

    result = 0
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            # 방문하지 않은 것 중에는 1도 있다.
            if not visited[i][j] and graph[i][j] == 0:
                result += 1
    return result

dfs(0, 0)
print(answer)