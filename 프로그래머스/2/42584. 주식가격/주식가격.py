def solution(prices):
    answer = [0] * len(prices)
    
    # 매초(=인덱스)마다 기록된 가격
    # 해당 가격을 유지한 시간을 그대로 리턴
    
    stack = [] # (인덱스, 진입시간)
    curr = 0
    for time, price in enumerate(prices): #([0, 1, 2, ...], [n, n, n, ...])
        while stack and prices[stack[-1][0]] > price: # 현재 값이 이전 값보다 작으면
            p, q = stack.pop() # 스택 pop()
            answer[p] = curr - q # pop()한 값의 해당하는 인덱스의 유지 시간 계산
        stack.append((time, curr))
        curr += 1
    
    while stack:
        p, q = stack.pop()
        answer[p] = curr - q - 1 # curr +=1 한 값이므로 -1 해줌
    
    return answer