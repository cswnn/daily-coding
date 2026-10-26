from collections import Counter
def solution(topping):
    answer = 0
    
    # 롤케이크 공평하게 나누기
    # 크기, 토핑 개수 상관 X
    # 토핑 가짓수가 중요
    
    # 세트 사용
    # 공평하게 나눌 수 있는 경우의 수 리턴하기
    # 단, 불가능(0)할 수도 있음
    # 두 조각 만들면 됨
    set_A = set()
    dict_B = Counter(topping)
    
    for i in topping:
        # if len(set(topping[:i])) == len(set(topping[i:])): # 절반 넘어가면 종료
        if i not in set_A:
            set_A.add(i)
        dict_B[i] -= 1
        if dict_B[i] == 0:
            del dict_B[i]
        
        if len(set_A) == len(dict_B):
            answer += 1
    
    return answer