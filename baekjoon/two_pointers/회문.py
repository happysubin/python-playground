n = int(input())

def similar_pal(arr):
    lt = 0
    rt = len(arr) - 1
    while lt < rt:
        if arr[lt] == arr[rt]:
            lt += 1
            rt -= 1
        else:
            if is_pal(arr, lt, rt - 1):
                return True
            if is_pal(arr, lt + 1, rt):
                return True
            return False

    return False

def is_pal(arr, lt, rt):
    while lt < rt:
        if arr[lt] != arr[rt]:
            return False
        lt += 1
        rt -= 1
    return True


# 모두 같으면 회문 0
# 한문자를 삭제하여 회문으로 만들 수 있으면 유사 회문은 1
# 아니라면 그냥 2
for i in range(n): 
    arr = list(input())
    if is_pal(arr, 0, len(arr) - 1):
        print(0)
    elif similar_pal(arr):
        print(1)
    else:
        print(2)
    
# “진짜 삭제해보고 검사하자” X. 정석은 “삭제했다고 가정하고 포인터만 조정하자”야.