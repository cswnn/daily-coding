def solution(clothes):
    answer = 0
    
    # 서로 다른 의상 조합 경우의 수
    # *종류별 0~1가지 착용 가능
    # *하루에 1개 이상 반드시 착용
    # *같은 이름 없음
    # [[의상이름, 의상종류], ...]
    
    # 가능한 모든 경우의 수 - 하나도 안 입는 경우(1가지) = answer
    
    # 의상 종류별 개수 기록
    dict_clothes = {}
    for item, kind in clothes:
        if kind in dict_clothes:
            dict_clothes[kind] += 1
        else:
            dict_clothes[kind] = 2
    
    # 가능한 경우의 수 계산 및 -1
    total = 1
    for t in dict_clothes.values():
        total *= t
    
    answer = total - 1
    
    return answer