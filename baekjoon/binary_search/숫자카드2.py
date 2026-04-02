# 상근이가 가지고 있는 숫자 카드의 개수
n = input()
arr = list(map(int, input().split()))

arr.sort()
d = {}
for i in range(len(arr)):
    d[arr[i]] = d.get(arr[i], 0) + 1

# 상근이가 몇 개 가지고 있는지 구해야할 M개의 정수
m = input()
arr2 = list(map(int, input().split()))
result = [0]
keys = list(d.keys())

def binary_serach(index):
    left = 0
    right = len(keys) - 1
    target = arr2[index]

    while left <= right:
        mid = (left + right) // 2
        if keys[mid] == target:
            return d[keys[mid]]
        elif keys[mid] < target:
            left = mid + 1
        else :
            right = mid - 1
    return 0

answer = []
for i in range(len(arr2)):
    answer.append(binary_serach(i))

print(*answer)