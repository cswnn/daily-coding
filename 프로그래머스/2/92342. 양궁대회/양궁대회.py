def solution(n, info):
    answer = []
    
    # ========= 양궁대회 =========
    # 지난 우승자(라이언) 불리한 게임
    #    - k점에 대해 더 많이 맞춘 사람이 k점 가져감.
    #    - 여러 발 맞히더라도 k점.
    #    - 동점인 경우 '어피치'가 가져감
    #    - 모든 과녁에 대해 각각 계산
    # 최종 결과 동점인 경우 '어피치' 우승
    # ==========================
    
    ### 라이언이 가장 큰 점수차로 우승하기 위해 맞혀야 하는 과녁 점수(정수 배열) 리턴
    # 무조건 라이언이 이길 수 없는 경우 [-1] 리턴
    # 여려 경우가 있을 때는 가장 낮은 점수를 더 많이 맞힌 경우를 리턴
    
    '''
    01) 라이언이 이길 수 있는가?
    02) 브루트포스 
    03) '어피치' 과녁을 보고 각 점수별 '라이언'이 득점하기 위해 필요한 화살 수 계산
    04) 득점에 필요한 화살수를 n개 안에서 경우의 수 만들어 계산
    05) 최고점을 만드는 과녁 출력(2개 이상일 경우 가장 낮은 점수 적중 횟수 순으로)
    '''
    
    # - (라이언 - 어치피) 점수차
    def cal_score(A: list, L: list):
        score = 10
        ap_score, li_score = 0, 0
        for a, l in zip(A, L):
            if a == l == 0:
                pass
            elif a < l:
                li_score += score
            else:
                ap_score += score
                
            score -= 1
        
        return li_score - ap_score
    
    # - 점수차 동일한 과녁 경우의 수 '우선' 계산 함수
    def eq_score(prv: list, nxt: list):
        for i in range(10, -1, -1):
            if prv[i] == nxt[i]:
                continue
            elif prv[i] < nxt[i]:
                return nxt
            else:
                return prv
        return prv
    
    def dfs(n: int, curr: int):
        print(lion)
        nonlocal max_score, answer
        # n: 현재 남은 화살 수
        # curr: 현재 계산 중인 점수
        # 10~0점 과녁까지 백트래킹 후 끝난 경우 해당 경우 리턴(Lion의 과녁 리스트)
        if curr >= 11:
            diff_score = cal_score(info, lion)
            if diff_score > 0: # 라이언이 이긴 경우
                if diff_score > max_score: # 최고 점수차로 갱신
                    max_score = diff_score
                    answer = lion.copy()
                elif diff_score == max_score:
                    res = eq_score(answer, lion)
                    answer = res.copy()
            return
        
        # 마지막 0점 과녁에 도달하면 화살 전부 털기
        if curr == 10:
            lion.append(n)
            dfs(0, curr + 1)
            lion.pop()
                
        # 아직 진행 중
        else:
            # 해당 점수 득점에 필요한 화살 있는 경우
            if n >= need_info[curr]:
                lion.append(need_info[curr])
                dfs(n - need_info[curr], curr + 1)
                lion.pop()
            # 해당 점수 득점하지 않는 경우
            lion.append(0)
            dfs(n, curr + 1)
            lion.pop()
                
    need_info = [s + 1 for s in info]
    lion = []
    max_score = 0
    
    dfs(n, 0)
    
    if not answer:
        return [-1]
    
    return answer