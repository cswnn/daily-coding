from collections import deque

def solution(maps):
    answer = 0
    
    # 동서남북 이동하여 상대 진영까지의 최단경로
    n = len(maps[0]) # 행
    m = len(maps) # 열
    visited = [[0] * n for _ in range(m)]
    
    def bfs(n, m):
        queue = deque([(0, 0)])
        
        dr = [0, 0, -1, 1]
        dc = [-1, 1, 0, 0]
        
        while queue:
            r, c = queue.popleft()
            
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                
                if 0 <= nr < m and 0 <= nc < n:
                    if visited[nr][nc] == 0 and maps[nr][nc] == 1: # 미방문 & 길
                        visited[nr][nc] = visited[r][c] + 1
                        queue.append((nr, nc))

    bfs(n, m)
    
    answer = visited[-1][-1] + 1 if visited[-1][-1] else -1
    
    return answer