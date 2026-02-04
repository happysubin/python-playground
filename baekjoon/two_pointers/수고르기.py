# n은 수열길이
# m 고른 두 수가 M 이상이면서 제일 작은 경우를 구하기
n, m = map(int, input().split())

arr = [ int(input()) for _ in range(n) ]

arr.sort()

lt = 0
rt = 0
answer = float('inf')

while rt < n:
    sum_value = arr[rt] - arr[lt]

    if sum_value > m:
        answer = min(sum_value, answer)
        lt += 1

    elif sum_value == m:
        answer = m
        break
    else:
        rt += 1
print(answer)

        


