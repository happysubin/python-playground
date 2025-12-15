from collections import Counter

def solution(participant, completion):
    c = Counter()
    for p in participant:
        c[p] += 1
    
    for co in completion:
        c[co] -= 1
    return c.most_common(1)[0][0]

def solution2(participant, completion):
    answer = Counter(participant) - Counter(completion)
    return list(answer.keys())[0]