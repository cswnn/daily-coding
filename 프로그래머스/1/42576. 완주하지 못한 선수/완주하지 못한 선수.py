def solution(participant, completion):
    answer = ''
    
    check = dict()
    
    for p in participant:
        if p in check:
            check[p] += 1
        else:
            check[p] = 1
    
    for c in completion:
        if c in check:
            check[c] -= 1
    
    for k, v in check.items():
        if v == 1:
            answer = k
            break
    
    return answer