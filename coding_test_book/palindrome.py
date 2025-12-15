
# 영문자, 숫자만을 대상으로 하는 팰린드롬
import collections
import re
from typing import Deque


def palindrome(str: str) -> bool:
    strs = []
    for char in str:
        if char.isalnum():
            strs.append(char.lower())

    # pop은 제거하면서 반환
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False
    return True        

def palindromeV2(str: str) -> bool:
    strs: Deque = collections.deque() # 자료 구조를 변경해 성능 향상. 리스트는 연속된 메모리 배열이라 첫번째 요소를 제거하면 한칸씩 옮기기 때문. deque는 포인터만 조정
    for char in str:
        if char.isalnum():
            strs.append(char.lower())

    # pop은 제거하면서 반환
    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False
    return True         

def palindromeV3(str: str) -> bool:
    str = str.lower()
    str = re.sub('[^a-z0-9]', '', str)
    return str == str[::-1]           

print(palindrome("Hi"))
print(palindromeV2("Hi"))
print(palindromeV3("Hi"))

print(palindrome("SOS"))
print(palindromeV2("SOS"))
print(palindromeV3("SOS"))