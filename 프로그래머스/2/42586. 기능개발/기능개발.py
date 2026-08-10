def solution(progresses, speeds): 
    '''작업 진도와 작업 속도를 받아 각 배포마다 배포되는 기능 개수 반환'''
    answer = []
    
    # 차례로 작업 배포 일수 계산 후 바로 뒤 작업 완료되는지 계산
    # for p, s in zip(progresses, speeds):
    cnt, idx = 1, 0
    while idx < len(progresses) and idx + cnt < len(progresses):
        if cnt == 1:
            need_days = ((100 - progresses[idx]) + (speeds[idx] - 1)) // speeds[idx]
        next_need_days = ((100 - progresses[idx + cnt]) + (speeds[idx + cnt] - 1)) // speeds[idx + cnt]
        if next_need_days <= need_days:
            cnt += 1
        else:
            idx += cnt
            answer.append(cnt)
            cnt = 1
    
    answer.append(cnt)
    
    return answer