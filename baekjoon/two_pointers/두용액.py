x = int(input())
arr = list(map(int, input().split()))

arr.sort()

lt = 0
rt = len(arr) - 1

min_value = float('inf')
r1 = arr[0]
r2 = arr[1]
while lt < rt:
    compared = arr[lt] + arr[rt]    
    if(abs(compared) < min_value):
        min_value = abs(compared)
        r1 = arr[lt]
        r2 = arr[rt]

    if compared < 0:
        lt += 1
    else:
        rt -=1

print(r1, r2)    

