from itertools import permutations

def solution(k, dungeons):
    answer = -1
    
    # 탐험할 수 있는 최대 던전 수 출력
    for cases in permutations(dungeons):
        _k = k
        cnt = 0
        # print(cases)
        # print("=====")
        for need, consume in cases:
            # print(need, consume)
            if need <= _k:
                # print(_k, need, consume)
                _k -= consume
                cnt += 1
            else:
                # answer = cnt
                break
                # print(cases, cnt)
        answer = max(answer, cnt)
        # print(cnt)
    
    return answer