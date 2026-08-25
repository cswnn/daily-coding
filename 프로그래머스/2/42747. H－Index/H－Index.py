def solution(citations):
    answer = 0
    
    # Goal: h번 이상 인용된 논문이 h편 이상이 되는 최대값 h 찾기
           
    # 내림차순 정렬하고 0번부터 시작
        # 01. 인덱스가 크면 인용횟수를 현재 H-index와 비교
        # 02. 인용횟수가 크면 인덱스를 현재 H-index와 비교
    
    n = len(citations)
    citations.sort(reverse=True)
    
    for i, h in enumerate(citations):
        # if i + 1 >= h:
        #     answer = max(h, answer)
        #     break
        # else:
        #     answer = max(i + 1, answer)
        answer = max(min(i + 1, h), answer)
        if h < i + 1:
            break
    
    return answer