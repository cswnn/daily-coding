def solution(numbers, target):
    answer = 0
    
    # n개의 수를 순서 그대로 더하거나 빼서 target 만들고, 가능한 방법 수 리턴
    # 길이: 2이상 20이하, 각 숫자: 1이상 50이하, 타겟: 1이상 1000이하
    
    # DFS 활용
    def dfs(present, total):
        if present < len(numbers):
            return dfs(present + 1, total + numbers[present]) \
                    + dfs(present + 1, total - numbers[present])
        else:
            return 1 if total == target else 0
    
    answer = dfs(0, 0)
            
    return answer