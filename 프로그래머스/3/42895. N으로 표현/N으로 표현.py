def solution(N, number):
    answer = -1
    
    # number을 만들기 위해 필요한 N의 최소 개수.
    # + - * /
    
    # 01) N으로 만들 수 있는 수들
    # 02) 1 ~ number 까지 만들기.
    
    # **8개 N으로 만들 수 있는 모든 수 만들고**
    # 그중에 number 있으면 해당하는 값 리턴 or not -1 리턴
    
    dp = [set() for _ in range(9)]
    
    for i in range(1, 9):
        dp[i].add(int(str(N) * i))
    
    for i in range(1, 9):
        for j in range(1, i):
            for op1 in dp[j]:
                for op2 in dp[i - j]:
                    dp[i].add(op1 + op2)
                    dp[i].add(op1 - op2)
                    dp[i].add(op1 * op2)
                    if op2 != 0:
                        dp[i].add(op1 // op2)
        
        if number in dp[i]:
            return i
    
    # answer = -1 if answer > 8 else answer
    
    return answer