from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    ### 모든 트럭이 다리를 건너는 데 필요한 최소 시간 리턴
    # 트럭의 순서는 정해져 있음
    
    truck_weights = deque(truck_weights)
    on_bridge = deque([0] * bridge_length) # 현재 다리 상태
    
    # 현재 다리 위 무게를 기준으로 다음 트럭의 무게 계산
    while truck_weights:        
        # 내리는 동시에 타는 경우를 계산하기 위해서 먼저 뺄셈
        weight += on_bridge.popleft()

        # 다음 트럭이 올라갈 여유 되는 경우
        if weight >= truck_weights[0]:
            next_truck = truck_weights.popleft()
            weight -= next_truck
            # weight += on_bridge.popleft()
            on_bridge.append(next_truck)
            
        # 다음 트럭이 올라갈 여유 없는 경우
        else:
            # weight += on_bridge.popleft()
            on_bridge.append(0)
        
        # 시간 +1
        answer += 1
    
    # 마지막 트럭이 올라탔을 때
    answer += bridge_length
    
    return answer