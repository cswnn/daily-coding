import heapq

def solution(scoville, K):
    answer = 0
    
    # 최소 스코빌이 k이상이 될 때까지 믹스.
    
    heapq.heapify(scoville)
    # 목표 도달하거나 믹스할 수 없을 때까지
    while scoville[0] < K and len(scoville) >= 2:
        small = heapq.heappop(scoville)
        big = heapq.heappop(scoville)
        
        heapq.heappush(scoville, big*2 + small)
        answer += 1
    
    # 목표 미달
    if scoville[0] < K:
        answer = -1
    
    return answer