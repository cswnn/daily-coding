def solution(numbers):
    answer = ''
    
    # 수 이어 붙여 가장 큰 수 만들기
    # 각 원소는 1000 이하
    # 출력은 문자열 타입으로
    
    _numbers = [str(i) for i in numbers]
    _numbers.sort(key = lambda x : x * 3, reverse=True)
    
    # answer = str(int("".join(_numbers)))
    answer = "".join(_numbers).lstrip('0') or '0'

    
    return answer