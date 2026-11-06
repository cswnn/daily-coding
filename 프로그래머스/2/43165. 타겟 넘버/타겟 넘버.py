def solution(numbers, target):
    answer = 0
    
    # +, - 해서 타겟넘버 만들 수 있는 경우의 수 출력
    
    n = len(numbers)
    
    def dfs(curr, N, total):
        nonlocal answer
        
        if curr < n:
            dfs(curr + 1, N, total + numbers[curr])
            dfs(curr + 1, N, total - numbers[curr])
        else:
            if total == target:
                answer += 1
    
    dfs(0, n, 0)
        
    return answer