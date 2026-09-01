def solution(brown, yellow):
    answer = []
    
    # 테두리 개수, 내부 개수로 전체 카펫 크기 [{가로}, {세로}] 리턴
    # 가로 >= 세로
    
    # 2w + 2h - 4 = brown
    # (w - 2) x (h - 2) = yellow
    # 2w = brown - 2h + 4
    # w = brown//2 - h + 2
    # (brown - h + 2) x (h - 2) = yellow
    
    # 최저 길이부터 최대 길이까지 반복(완전) 탐색
    for w in range(3, brown // 2):
        h = brown // 2 - w + 2
        # print(w, h)
        if (w - 2) * (h - 2) == yellow:
            answer = [max(w, h), min(w, h)]
            break
    
    return answer