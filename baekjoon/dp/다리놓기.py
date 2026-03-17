t = int(input())

dp = [[0] * 31 for _ in range(31)]

# 초기값. 
for m in range(1, 31):
    dp[1][m] = m
    dp[m][m] = 1


# 점화식
for n in range(2, 31):
    for m in range(n + 1, 31):
        dp[n][m] = dp[n - 1][m - 1] + dp[n][m - 1]

for _ in range(t):
    n, m = map(int, input().split())
    print(dp[n][m])