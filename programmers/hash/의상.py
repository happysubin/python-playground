from collections import * 

def solution(clothes):
    c = Counter()
    answer = 1
    for i in range(len(clothes)):
        key = clothes[i][1]
        c[key] += 1 

    for i in list(c.values()):
        answer *= (i + 1) 
    
    return answer - 1