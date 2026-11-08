from collections import deque
def solution(n, wires):
    answer = n
    
    # 트리를 끊어 두 네트워크의 송전탑 개수 차이의 절대값이 최소가 되게
    unconnect = [[0] * (n+1) for _ in range(n+1)]

    # 개수 세기 함수
    def bfs(m):
        queue = deque([m])
        visited = [0] * (n + 1)
        visited[m] = 1
        while queue:
            k = queue.popleft()
            
            for i, j in wires:
                if unconnect[i][j]:
                    continue
                if k == i and not visited[j]:
                    visited[j] = 1
                    queue.append(j)
                elif k == j and not visited[i]:
                    visited[i] = 1
                    queue.append(i)
        
        return sum(visited)
    
    # 하나씩 끊어보기
    for a, b in wires:
        # print(a, b)
        unconnect[a][b] = unconnect[b][a] = 1
        r = abs(bfs(a) - bfs(b))
        # print(r)
        answer = min(answer, r)
        unconnect[a][b] = unconnect[b][a] = 0
    
    return answer