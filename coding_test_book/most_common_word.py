from collections import Counter
import re


def find_common_word(banned: list[str], str: str) -> str:
    c = Counter()
    strr = str.lower()
    for s in re.split(r'[,\s]+', strr):
        if s not in banned:
            c[s] += 1

    return c.most_common(1)[0][0]

banned = ["hit"]
str = "Bob hit a ball, the hit BALL flew far after it was hit"
print(find_common_word(banned, str))