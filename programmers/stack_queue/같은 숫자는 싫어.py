from collections import deque

def solution(arr):
    stack = deque()
    for i in range(len(arr)):
        # 맨 위 값 조회
        if stack and stack[-1] == arr[i]:
            continue
        else:
            stack.append(arr[i])    
    return list(stack)


print(solution([1, 1, 3, 3, 0, 1, 1]))
print(solution([4, 4, 4, 4, 3, 3]))
