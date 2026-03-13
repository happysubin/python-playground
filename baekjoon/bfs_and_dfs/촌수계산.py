import sys
from collections import deque
input = sys.stdin.readline

# 전체 사람 수
total = int(input())

# 촌수 계산해야하는 서로 다른 두사람
start, goal = map(int, input().split())

edges = int(input())

family = [[] for _ in range(total + 1)]
visited = [False] * (total + 1)

for i in range(edges):
    # x는 자식, y는 부모
    x, y = map(int, input().split())

    family[x].append(y)
    family[y].append(x)

queue = deque()

queue.append((start, 0))

flag = False

while queue:
    next, cnt = queue.popleft()
    if next == goal:
        print(cnt)
        flag = True
        break

    for n in family[next]:
        if not visited[n]:
            visited[n] = True
            queue.append((n, cnt + 1))


if not flag:
    print(-1)