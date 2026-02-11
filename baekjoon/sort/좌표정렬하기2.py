n = int(input())

list = []
for _ in range(n):
    x, y = map(int, input().split())
    list.append((x, y))

list.sort(key = lambda x: (x[1], x[0]))

# y 좌표가 증가하는 순, X 좌표가 증가하는 순
for x, y in list:
    print(x, y)