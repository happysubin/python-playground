n = input()
arr = list(map(int, input().split()))
m = input()
arr2 = list(map(int, input().split()))

arr.sort()

def binary_search(index):
    left = 0 
    right = len(arr) - 1
    target = arr2[index]

    while left <= right:
        mid = (left + right) // 2
        if target == arr[mid]:
            return 1
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1 
    return 0

for i in range(len(arr2)):
    print(binary_search(i))


