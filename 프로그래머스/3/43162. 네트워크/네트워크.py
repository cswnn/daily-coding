def solution(n, computers):
    answer = 0
    
    ## 네트워크(연결된 덩어리) 개수 리턴
    
    visited = [0] * n
    
    def dfs(v):
        visited[v] = 1 # 방문 처리
        for next_v in range(n):
            # 연결 O, 방문 X
            if not visited[next_v] and computers[v][next_v]:
                dfs(next_v)

    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
    
    return answer
