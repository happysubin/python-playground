n = int(input())

arr = list(map(int, input().split()))

lt = 0
rt = len(arr) - 1

result = float('inf')
while lt < rt:
    diff = arr[rt] + arr[lt]
    if abs(diff) < abs(result):
        result = diff

    if diff > 0:
        rt -= 1
    else :
        lt += 1

print(result)

