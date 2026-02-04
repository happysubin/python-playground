n = int(input())
arr = list(map(int, input().split()))

lt = 0
rt = n - 1

r1 = 0
r2 = 0

min_value = float('inf')

while lt < rt:
    diff = arr[lt] + arr[rt]

    if abs(diff) < min_value:
        min_value = abs(diff)
        r1 = arr[lt]
        r2 = arr[rt]

    if diff > 0:
        rt -= 1
    else:
        lt += 1

print(r1, r2)