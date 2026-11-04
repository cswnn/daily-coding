from itertools import permutations
def solution(numbers):
    answer = 0
    
    s = set()
    for i in range(1, len(numbers)+1):
        for num in permutations(numbers, i):
            t = int("".join(num))

            if t in s or t == 0 or t == 1:
                continue
            s.add(t)

            cnt = 0
            for j in range(2, int(t**(1/2)) + 1):
                if t % j == 0:
                    cnt += 1
                    break
            if cnt <= 0:
                answer += 1
    
    return answer