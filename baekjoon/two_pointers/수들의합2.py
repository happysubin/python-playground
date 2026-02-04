temp = list(map(int, input().split()))

n = temp[0] # 수열 길이
m = temp[1] # 목표

arr = list(map(int, input().split()))


lt = 0
rt = 0

sum = 0
answer = 0

while rt <= n:
    if sum < m:
        if rt == n:
            break
        sum += arr[rt]
        rt += 1
    elif sum > m:
        sum -= arr[lt]
        lt += 1
    else :
        answer += 1
        sum -= arr[lt]
        lt += 1

print(answer)