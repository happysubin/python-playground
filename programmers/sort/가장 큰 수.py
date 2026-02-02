def solution(numbers):
    # map(함수, 반복가능한것)
    str_arr = list(map(str, numbers))
    # 3과 30이 있다면 333, 303030 을 문자열 기준으로 비교
    str_arr.sort(key=lambda x: x*3, reverse=True)
    answer = ''
    for i in range(len(str_arr)):
        answer += str_arr[i]
    return str(int(answer))


print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))