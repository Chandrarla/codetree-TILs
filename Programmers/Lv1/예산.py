# 최대한 많은 부서의 물품 구매, 신청한 금액만큼 모두 지원
def solution(d, budget):
    sum = 0
    count = 0  # 승인된 부서의 수를 세기 위한 변수
    sorted_d = sorted(d)  # 최대로 지원 가능한 부서의 수만 알면 되기에 요청 금액을 오름차순으로 정렬

    for i in sorted_d:
        if sum + i <= budget:  # 현재까지의 합계에 다음 요청 금액을 더한 값이 예산 이하인 경우
            sum += i  # 합계를 업데이트
            count += 1  # 승인된 부서의 수를 증가
        else:  # 예산을 초과하는 경우 탈출
            break
    return count

ans = solution([2,2,3,3], 10)
print(ans)

# ----- 오답 -----
# def solution(d, budget):
#     sum = 0
#     sorted_d = sorted(d)
#     for i in range(len(d)):
#         if sum > budget:
#             return i-1
#         sum += sorted_d[i]
#     if sum <= budget:
#         return len(d)