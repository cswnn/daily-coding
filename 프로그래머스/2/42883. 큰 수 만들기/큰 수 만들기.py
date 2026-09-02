def solution(number, k):
    answer = ''
    
    # 어떤 숫자에서 k개의 수를 제거 했을 때 얻을 수 있는 가장 큰 숫자
    # 01. 숫자 1개 빼서 가장 큰 숫자를 남기기 -> k번 반복 ===> 런타임에러
    # 02. 앞자리부터 K개 이하 빼서 맨 앞에 오게 할 수 있는 가장 큰 수 까지 빼기
    #     - 현재가 가장 크면 패스
    #     - 그 다음 자리부터 k개 뺄 때까지 반복
    # 03. [해설 참고] 스택 사용. 앞에서부터 모든 숫자에 대해 자신이 앞자리보다 큰 수면 앞자리 수 제침
    stack = []
    for num in number:
        while stack and k > 0 and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)
        
    if k > 0:
        stack = stack[:-k]
    
    answer = "".join(stack)
    # 01 ====================
    # for _ in range(k):
    #     max_n = ''
    #     _number = str(number)
    #     n = len(_number)
    #     for i in range(n):
    #         if i == 0:
    #             # next_n = int(_number[1:])
    #             next_n = _number[1:]
    #         elif i == n - 1:
    #             # next_n = int(_number[:-1])
    #             next_n = _number[:-1]
    #         else:
    #             # next_n = int(_number[:i] + _number[i+1:])
    #             next_n = _number[:i] + _number[i+1:]
    #         # next_n = int(_number[:i] + _number[i+1:])
    #         max_n = max(max_n, next_n)
    #     number = max_n
    #     answer = max_n
    #     # print(answer)
    
    # 02 ====================
#     start = 0
#     while k > 0:
#         max_idx = start
#         max_val = number[max_idx]
#         for i in range(max_idx + 1, max_idx + 1 + k):
#             if number[i] > max_val:
#                 max_idx = i
#                 max_val = number[i]
        
#         # 맨 앞자리가 최대값
#         if max_idx == 0:
#             start += 1
#         # 최대값 찾은 경우
#         else:
#             start += max_idx
#             number = number[max_idx:]
#             k -= max_idx
            
#     answer = max_val
    
    return answer