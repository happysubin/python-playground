import math
def solution(progresses, speeds):
    answer = []
    # 1. 모든 작업들이 언제 끝나는지 날짜를 계산
    days = []
    for i in range(len(progresses)):
        day = (100 - progresses[i]) / speeds[i]
        days.append(math.ceil(day))
    
    idx = 0
    max = days[0]
    # 2. 배포 날 비교
    for i in range(len(days)):
        # 차피 0이 수행 1로 올라감
        if max >= days[i]:
            idx += 1
        else :
            # 일괄 처리
            answer.append(idx)
            # 새로운 배포 그룹
            max = days[i]
            idx = 1
    
    # 마지막 남은 그룹 처리
    answer.append(idx)
    return answer

print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))