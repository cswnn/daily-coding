from itertools import permutations

def solution(k, dungeons):
    answer = -1
    
    _k = k
    
    # 탐험할 수 있는 최대 던전 수 리턴
    for p in permutations(dungeons):
        cnt = 0
        for least, take in p:
            if k >= least:
                cnt += 1
                k -= take
            else:
                break
        k = _k
        
        answer = max(cnt, answer)
    
    return answer