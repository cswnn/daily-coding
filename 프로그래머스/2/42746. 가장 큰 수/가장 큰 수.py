def solution(numbers):
    answer = ''

    # 수어진 정수를 이어붙여 만들 수 있는 가장 큰 수 리턴
    
    # 1. 앞자리가 큰 순으로 정렬 [67, 6, 113, 1000]
    # 2. 자리수가 다르면 짧은 수는 거기서 멈추고 이어서 비교 [678, 6, 65, 652]
    # ---------------
    ### 서로 다른 자릿수의 각 정수 맨 앞자리를 어떻게 비교?
    # print("65" > "612") -> True : 문자열 타입으로 바꿔서
    # ---------------
    ### 30보다 3이 먼저와야 함을 어떻게 구현? 
    # print("3" > "30") -> False
    # print("333" > "303030") -> True : 자기 자신을 이어 붙이기
    
    # _numbers = [str(n) for n in numbers]
    _numbers = list(map(str, numbers))
    _numbers.sort(key = lambda x: x * 3, reverse=True)
    # print(_numbers)
    
    # answer = str(int(answer)) # 0 제거 -> 런타임 에러 발생
    ### cnt를 사용해 앞부분부터 0 세기 -> 모든 수가 0이지 않는 한 맨앞에 0 올 수 없음.
    # cnt = 0
    # while cnt < len(_numbers) and _numbers[cnt] == "0":
    #     cnt += 1
    answer = "".join(_numbers)
    answer = "0" if answer[0] == "0" else answer # 맨앞이 0 이라면 모든 원소가 0일 것임
    
    return answer