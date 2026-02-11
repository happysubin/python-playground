n = int(input())

list = []
for i in range(n):
    age, name = input().split()
    list.append((i, int(age), name))

list.sort(key = lambda x:(x[1], x[0]))


for i, age, name in list:
    print(age, name)