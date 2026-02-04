# n개의 서로 다른 양의 정수 a1, a2, ..., an으로 이루어진 수열이 있다. ai의 값은 1보다 크거나 같고, 1000000보다 작거나 같은 자연수이다. 자연수 x가 주어졌을 때, ai + aj = x (1 ≤ i < j ≤ n)을 만족하는 (ai, aj)쌍의 수를 구하는 프로그램을 작성하시오.
# https://www.acmicpc.net/problem/3273
temp = int(input())
arr = list(map(int, input().split()))
x = int(input())

# X는 J 미만 (이하가 아님)
arr.sort()
answer = 0 
lt = 0
rt = len(arr) - 1
while lt < rt:
    if arr[lt] + arr[rt] == x:
        answer += 1
        # 쌍이니까 중복을 고민하지 않아도 된다.
        lt += 1
        rt -= 1
    elif arr[lt] + arr[rt] > x:
        # 큰 수를 줄인다.
        rt -= 1
    else: # X보다 두 수의 합이 작은 경우, 큰 수를 키워야한다.
        lt += 1
print(answer)


# “정렬 + 양끝에서 좁혀가는 문제”