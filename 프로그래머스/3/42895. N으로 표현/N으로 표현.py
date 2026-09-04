def solution(N, number):
    answer = -1
    
    # number을 만들기 위해 필요한 N의 최소 개수.
    # + - * /
    
    # 01) N으로 만들 수 있는 수들
    # 02) 1 ~ number 까지 만들기.
    
    # **8개 N으로 만들 수 있는 모든 수 만들고**
    # 그중에 number 있으면 해당하는 값 리턴 or not -1 리턴
    
    dp = [set() for _ in range(9)]
    
    # for i in range(1, 9):
    #     dp[i].add(int(str(N) * i))
    
    for i in range(1, 9):
        dp[i].add(int(str(N) * i))
        for j in range(1, i):
            for op1 in dp[j]:
                for op2 in dp[i - j]: # -> 핵심: i개로 만들 수 있는 수는 str(N) * i와, {i-j로 만들 수 있는 수} {+|-|*|/} {j개로 만들 수 있는 수}로 모두 표현됨. 이때 0으로 나눠지는 경우만 유의.
                    dp[i].add(op1 + op2)
                    dp[i].add(op1 - op2)
                    dp[i].add(op1 * op2)
                    if op2 != 0:
                        dp[i].add(op1 // op2)
        
        if number in dp[i]:
            return i
    
    # answer = -1 if answer > 8 else answer
    
    return answer