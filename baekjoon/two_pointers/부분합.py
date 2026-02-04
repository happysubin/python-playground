temp = list(map(int, input().split()))
arr = list(map(int, input().split()))

n = temp[0] # 수열 길이
s = temp[1] # S 이상이 되는 것을 찾아야한다.

lt = 0
rt = 0

result = [0, 0] # 인덱스 0은 sum, 1은 len
min_len = 5000000

# 확장 이후 수축도 기다려봐야한다.
while rt <= n:
    if(result[0] < s):
        if rt == n:
            break
        result[0] += arr[rt]
        result[1] += 1
        rt += 1
    elif(result[0] >= s):
        if result[1] < min_len:
            min_len = result[1]
        result[0] -= arr[lt]
        result[1] -= 1  
        lt += 1

if min_len == 5000000:
    print(0)
else:
    print(min_len)  
    

