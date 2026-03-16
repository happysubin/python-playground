
from collections import deque

size = int(input())
r1, c1, r2, c2 = map(int, input().split())

queue = deque()
visited = [[False] * size for i in range(size)]

queue.append((r1, c1, 0))
visited[r1][c1] = True
flag = False

while queue:
    r, c, cnt = queue.popleft()

    if r == r2 and c == c2:
        print(cnt)
        flag = True
        break

    for (rx, rc) in [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]:
        next_r = r + rx
        next_c = c + rc
    
        if next_r >= 0 and next_r < size and next_c >= 0 and next_c < size:
            if not visited[next_r][next_c]: 
                visited[next_r][next_c] = True
                queue.append((next_r, next_c, cnt + 1))

if not flag:
    print(-1)