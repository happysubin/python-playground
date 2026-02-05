import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(now):
    visited[now] = True
    nxt = arr[now]
    if not visited[nxt]:
        dfs(nxt)

test_case = int(input())

for _ in range(test_case):
    size = int(input())
    arr = [0] + list(map(int, input().split()))  # 1-index
    visited = [False] * (size + 1)

    answer = 0
    for i in range(1, size + 1):
        if not visited[i]:
            answer += 1      # 새로 시작 = 새로운 사이클(컴포넌트) 1개
            dfs(i)

    print(answer)
