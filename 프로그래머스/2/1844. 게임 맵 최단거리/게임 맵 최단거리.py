from collections import deque
def solution(maps):
    answer = 0
    
    ### 상대팀 진영까지의 최단 거리 리턴
    
    # BFS, 상하좌우, visited
    # 최대 100x100, 0: 벽, 1: 길
    # 시작 위치: (1, 1), 상대 진영(n, m)
    n = len(maps)
    m = len(maps[0])
    
    # 방문, 최단거리 기록
    visited = [[0] * m for _ in range(n)]
    
    def bfs(r, c):
        visited[r][c] = 1
        queue = deque([(r, c)])
        
        # 상하좌우
        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]
        
        while queue:
            # 현재 위치
            a, b = queue.popleft()
            for i in range(4):
                nr = a + dr[i]
                nc = b + dc[i]
                # 게임 맵 벗어나지 않고, 미방문, 길o(벽x)
                if 0 <= nr < n and 0 <= nc < m and \
                    not visited[nr][nc] and maps[nr][nc]:
                    visited[nr][nc] = visited[a][b] + 1
                    queue.append((nr, nc))
        
    bfs(0, 0)
    answer = visited[-1][-1] if visited[-1][-1] else -1
    
    return answer