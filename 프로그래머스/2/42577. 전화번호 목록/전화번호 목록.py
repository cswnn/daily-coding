def solution(phone_book):
    answer = True
    
    # 자기자신의 일부를 잘라 목록에 있는지 확인
    # 중복 x
    
    # 번호길이 순 정렬 필요한가? - 아닐 거 같음
    
    # 해시 탐색용 집합
    _phone_book = set(phone_book) 
    
    # 길이 1부터 자기자신 길이-1까지 모든 경우의 수 반복.
    for num in phone_book:
        n = len(num)
        for i in range(1, n): # 자기자신과 동일 제외한 모든 자릿수
            if num[0 : i] in _phone_book:
                return False

    return True 