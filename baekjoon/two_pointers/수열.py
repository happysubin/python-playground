
temp = list(map(int, input().split()))

n = temp[0]
k = temp[1]

arr = list(map(int, input().split()))

result = [0, 0] # 인덱스 0은 합, 1은 길이

# 슬라이딩 윈도우 초기화
cur_sum = sum(arr[:k])
max_value = cur_sum

for i in range(k, n):
    cur_sum = cur_sum - arr[i-k] + arr[i]
    max_value = max(max_value, cur_sum)


print(max_value)