# n은 고양이 수, max(k)는 버틸 수 있는 무게
n, max = map(int, input().split())
cats = list(map(int, input().split()))
answer = 0

cats.sort()
lt = 0
rt = len(cats) - 1

while lt < rt:
    if cats[lt] + cats[rt] > max:
        rt -= 1
    else:
        answer += 1
        rt -= 1
        lt += 1

print(answer)