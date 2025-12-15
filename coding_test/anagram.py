from collections import defaultdict

def anagram(strs: list[str]):
    dic = defaultdict(list)
    for s in strs:
        value = ''.join(sorted(s))
        dic[value].append(s)
    return list(dic.values())


print(anagram(["eat", "tea", "tan", "ate", "nat", "bat"]))        