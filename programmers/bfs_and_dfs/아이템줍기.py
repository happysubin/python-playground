from collections import deque


def bfs(map, start_x, start_y, goal_x, goal_y):
    queue = deque()
    visited = [[False] * 102 for _ in range(102)]
    answer = float('inf')
    queue.append((start_x, start_y, 0))
    visited[start_y][start_x] = True
    while queue:
        x, y, cnt = queue.popleft()

        if x == goal_x and y == goal_y:
            answer = min(cnt, answer)

        for (ax, ay) in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            temp_x = x + ax 
            temp_y = y + ay
            if temp_x >= 0 and temp_x < 102 and temp_y >= 0 and temp_y < 102:
                if map[temp_y][temp_x] == 1 and not visited[temp_y][temp_x]:
                    visited[temp_y][temp_x] = True
                    queue.append((temp_x, temp_y, cnt + 1))
    return answer // 2


def solution(rectangle, characterX, characterY, itemX, itemY):


    board = [[0]*102 for _ in range(102)]

    # 1) 사각형 영역 채우기(겹치면 1 유지)
    for x1, y1, x2, y2 in rectangle:
        x1, y1, x2, y2 = x1*2, y1*2, x2*2, y2*2
        for y in range(y1, y2+1):
            for x in range(x1, x2+1):
                board[y][x] = 1

    # 2) 내부 지우기 (테두리만 남기기)
    for x1, y1, x2, y2 in rectangle:
        x1, y1, x2, y2 = x1*2, y1*2, x2*2, y2*2
        for y in range(y1+1, y2):
            for x in range(x1+1, x2):
                board[y][x] = 0

    # 캐릭/아이템도 2배
    cx, cy, ix, iy = characterX*2, characterY*2, itemX*2, itemY*2

    return bfs(board, cx, cy, ix, iy) 

print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8))