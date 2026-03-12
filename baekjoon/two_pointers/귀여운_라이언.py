n, k = map(int, input().split())
arr = list(map(int, input().split()))

lt = 0

# 현재 윈도우(구간) 안에 포함된 라이언 인형(1)의 개수
cnt = 0

# 처음에는 아직 답을 못 찾았으니 무한대로 둠
result = float('inf')

# 오른쪽 포인터를 한 칸씩 늘려 가면서 구간을 확장
for rt in range(n):
    # 새로 포함된 값이 라이언 인형이면
    # 현재 구간 안의 라이언 개수를 1 증가
    if arr[rt] == 1:
        cnt += 1

    # 현재 구간 안에 라이언이 k개 이상 있으면 이 구간은 조건을 만족하는 구간임
    while cnt >= k:
        # 현재 구간 [lt ~ rt]의 길이를 구해서
        # 기존 정답보다 더 짧으면 갱신
        result = min(result, rt - lt + 1)

        # 이제 왼쪽 포인터를 줄여서
        # 더 짧은 구간도 가능한지 확인해 봄
        
        # 만약 lt가 라이언 인형이면
        # 구간에서 빠지므로 라이언 개수도 감소
        if arr[lt] == 1:
            cnt -= 1

        # 왼쪽 포인터를 오른쪽으로 한 칸 이동
        lt += 1

if result == float('inf'):
    print(-1)
else:
    print(result)