def solution(m, n, puddles):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    # 출발값은 1
    dp[1][1] = 1
        
    # 물 설정
    for z in range(len(puddles)):
        dp[puddles[z][1]][puddles[z][0]] = -1
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                continue
            # 물 무시
            if dp[i][j] == -1:
                continue
            # 위에가 물이 아니고, 왼쪽이 물인 경우
            if dp[i - 1][j] != -1 and dp[i][j - 1] == -1:
                dp[i][j] = dp[i - 1][j]
            # 왼쪽이 물이 아니고 위에가 물인 경우
            elif dp[i][j - 1] != -1 and dp[i - 1][j] == -1:
                dp[i][j] = dp[i][j - 1] 
            # 둘다 물인경우 
            elif dp[i][j - 1] == -1 and dp[i - 1][j] == -1:
                dp[i][j] = 0
            # 둘다 물이 아닌 경우
            else:
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

    return dp[n][m] % 1000000007