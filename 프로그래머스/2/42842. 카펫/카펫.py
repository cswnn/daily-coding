def solution(brown, yellow):
    answer = []
    
    # (노, 갈) 격자 개수로 전체 카펫 크기 리턴
    # n * m = b + y
    brown -= 4
    for i in range(brown//2 + 1):
        # e: 가로
        if i * (brown//2 - i) == yellow:
            answer = [(brown//2-i) + 2, i+2]
            break
    # (n-1) * (m-1) = yellow
    
    return answer