def solution(triangle):
    dp = [[0] * len(triangle) for _ in range(len(triangle))] 
    dp[0][0] = triangle[0][0]
    for i in range(1, len(triangle)):
        for j in range(i + 1):
            if j == 0:
                dp[i][j] = triangle[i][j] + dp[i - 1][j]
            elif j == i:
                dp[i][j] = triangle[i][j] + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(triangle[i][j] + dp[i - 1][j - 1], triangle[i][j] + dp[i - 1][j])
    
    return max(dp[len(triangle) - 1])