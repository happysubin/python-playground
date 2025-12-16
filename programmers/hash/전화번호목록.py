from collections import *

def solution(phone_book):
    arr = sorted(phone_book)
    for i in range(len(arr)):
        if i + 1 < len(arr):
            if arr[i + 1].startswith(arr[i]):
                return False    

    return True


def solution2(phone_book):
    phone_book.sort() # O(N log N)
    for i in range(len(phone_book) - 1): # 마지막 요소는 비교할 다음 요소가 없으므로 -1
        # arr[i+1]이 arr[i]로 시작하는지 확인
        if phone_book[i+1].startswith(phone_book[i]):
            return False    
    return True    