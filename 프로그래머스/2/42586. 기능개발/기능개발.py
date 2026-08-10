def solution(progresses, speeds): 
    '''작업 진도와 작업 속도를 받아 각 배포마다 배포되는 기능 개수 반환'''
    answer = []
    
#     # 01 차례로 작업 배포 일수 계산 후 바로 뒤 작업 완료되는지 계산
#     # for p, s in zip(progresses, speeds):
#     cnt, idx = 1, 0
#     while idx < len(progresses) and idx + cnt < len(progresses):
#         if cnt == 1:
#             need_days = ((100 - progresses[idx]) + (speeds[idx] - 1)) // speeds[idx]
#         next_need_days = ((100 - progresses[idx + cnt]) + (speeds[idx + cnt] - 1)) // speeds[idx + cnt]
#         if next_need_days <= need_days:
#             cnt += 1
#         else:
#             idx += cnt
#             answer.append(cnt)
#             cnt = 1
    
#     answer.append(cnt)

    # 02 남은 일수를 먼저 계산
    left = [
        (100 - p + (s - 1)) // s 
        for p, s in zip(progresses, speeds)
    ]

    curr_day = left[0]
    cnt = 0
    
    for day in left:
        if day <= curr_day:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
            curr_day = day
    
    answer.append(cnt)
    
    return answer