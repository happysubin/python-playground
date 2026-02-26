
# n은 구멍의 개수, m은 부피
# 구멍을 막기 위해 정학히 그 크기만큼의 부피를 소모
n, m = map(int, input().split())
arr = list(map(int, input().split()))

result = 0
window = 0
lt = 0
rt = 0

while rt < len(arr):
    if window < m:
        window += arr[rt]
        rt += 1  
    else :
        window -= arr[lt]
        lt += 1

    if window <= m:
        result = max(result, window)

print(result)