def solution(N, number):
    dp = [set() for _ in range(9)]  # dp[i]: N을 i번 써서 만들 수 있는 수들

    for i in range(1, 9):
        # 이어붙인 수 추가: N, NN, NNN ...
        dp[i].add(int(str(N) * i))

        # j개와 i-j개를 조합
        for j in range(1, i):
            for a in dp[j]:
                for b in dp[i - j]:
                    dp[i].add(a + b)
                    dp[i].add(a - b)
                    dp[i].add(a * b)
                    if b != 0:
                        dp[i].add(a // b)

        if number in dp[i]:
            return i

    return -1