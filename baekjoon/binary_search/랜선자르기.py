
# k는 랜선 갯수, 필요한 랜선 수
k, n = map(int, input().split())

arr = []
for i in range(k):
    arr.append(int(input()))

left = 1
right = max(arr)
answer = 0

while left <= right:
    mid = (left + right) // 2
    count = 0
    for line in arr:
        count += line // mid
    
    if count >= n:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)
    