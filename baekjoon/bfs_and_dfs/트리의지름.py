from collections import deque

# =========================
# 입력
# =========================

n = int(input())

# 인접 리스트 (1-indexed)
tree = [[] for _ in range(n + 1)]

# 트리는 간선이 n-1개
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    # 양방향 연결 + 가중치
    tree[a].append((b, c))
    tree[b].append((a, c))


# =========================
# 스택 DFS: 가장 먼 노드 찾기
# =========================
def farthest(start):

    # start로부터 각 노드까지의 거리
    # -1이면 아직 방문 안 함
    dist = [-1] * (n + 1)
    dist[start] = 0

    # (현재 노드, 부모 노드)
    stack = [(start, 0)]

    while stack:
        u, parent = stack.pop()

        # u와 연결된 이웃 노드 탐색
        for v, w in tree[u]:
            # 부모로 되돌아가는 간선은 무시
            if v == parent:
                continue

            # v는 처음 방문하므로 거리 계산
            dist[v] = dist[u] + w

            # 다음 탐색을 위해 스택에 push
            stack.append((v, u))

    # 가장 먼 노드 찾기
    far_node = 1
    for i in range(1, n + 1):
        if dist[i] > dist[far_node]:
            far_node = i

    print(dist)
    return far_node, dist[far_node]


# =========================
# 트리 지름 계산
# =========================

# 1️⃣ 아무 노드(1)에서 가장 먼 노드 찾기
u, _ = farthest(1)
print(u)
# 2️⃣ u에서 다시 가장 먼 거리 → 지름
_, diameter = farthest(u)

print(diameter)