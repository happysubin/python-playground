import sys

input = sys.stdin.readline

# n은 나무의 수 M은 나무의 길이
n, m = map(int, input().split())

trees = list(map(int, input().split()))

left = 1
right = max(trees)
answer = 0 

while left <= right:
    mid = (left + right) // 2
    sum = 0
    for tree in trees:
        if tree > mid:
            sum += tree - mid
    
    if sum >= m:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1 

print(answer)