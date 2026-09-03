from collections import deque

def solution(priorities, location):
    answer = 0
    
    # 일단 OUT, 우선순위 가장 높으면 실행, 아닌 건 다시 IN
    # 이때 location 위치 프로세스의 실행 순서 리턴
    
    queue = deque(priorities)
    cnt = 1
    
    while queue:
        # 일단 OUT
        pres = queue.popleft()
        
        # print(pres)
        # print(queue)
        
        # 자기자신이 마지막까지 남은 경우
        if not queue:
            answer = cnt
            break
            
        # 최우선순위인가?
        if pres >= max(queue):
            # 찾는 프로세스인가?
            if location == 0:
                answer = cnt
                break
            else:
                location -= 1
                cnt += 1
                
        else:
            queue.append(pres)
            location = location - 1 if location > 0 else len(queue) - 1
    
    return answer