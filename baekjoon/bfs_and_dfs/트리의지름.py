from collections import deque

# 노드의 개수
n = int(input())
answer = 0

# 이건 0을 사용 안하기 위함
tree = [[] for _ in range(n + 1)]


# 이건 n - 1번 만큼
for i in range(n - 1):
    a, b, c = map(int, input().split())
    tree[a].append((b, c))
    tree[b].append((a, c))

def dfs(start, visited, cnt) -> int: 
    result = cnt
    for c, c_value in tree[start]:
        if not visited[c]:
            visited[c] = True 
            result = max(result, dfs(c, visited, cnt + c_value))
    return result

# 모드 ㄴ노드에서 한번씩은 수행
for i in range(1, n + 1):
    visited = [False] * (n + 1)
    answer = max(answer, dfs(i, visited, 0))

print(answer)