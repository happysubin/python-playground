import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))

cur = arr[0]
ans = arr[0]

for i in range(1, n):
    cur = max(cur + arr[i], arr[i])
    ans = max(ans, cur)

print(ans)