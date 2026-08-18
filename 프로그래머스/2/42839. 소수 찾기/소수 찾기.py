from itertools import permutations

def solution(numbers):
    answer = 0
    
    # 종이 조각을 붙여 만들 수 있는 소수의 개수 리턴
    # 0~9 사이 숫자가 적힌 최대 7장의 조각
    
    # 중복 체크용 집합
    prime = set()
    
    # 1조각부터 모든 조각을 합친 경우까지
    for i in range(1, len(numbers) + 1):
        # 순서를 고려한 모든 경우의수 조합
        for n in permutations(numbers, i):
            num = int("".join(n))
            # 중복 체크
            if num not in prime:
                prime.add(num)
                # 0, 1 제외
                if num == 0 or num == 1:
                    continue
                # 2부터 자기 자신의 제곱근까지 나눠떨어지는 숫자 체크(= 소수체크)
                for s in range(2, int(num**(1/2)) + 1):
                    if num % s == 0:
                        break
                # 소수이면 +1
                else:
                    print(num)
                    answer += 1
    
    return answer