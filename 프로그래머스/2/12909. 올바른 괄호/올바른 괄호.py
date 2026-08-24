def solution(s):
    answer = True
    
    # () 짝이 맞게 닫히도록
    # *괄호 닫으려면 반드시 앞에서 열려있어야 함.
    
    # 리스트화
    _s = list(map(str, s))

    # 괄호 검사 (역순)
    stack = [] 
    while _s:
        t = _s.pop()
        if t == ')':
            stack.append(True)
        elif t == '(':
            if stack:
                stack.pop()
            else:
                return False
    
    # 열리지 않고 닫힌 경우(= 아직 닫기 괄호가 스택에 남아있음)
    if stack:
        return False

    return True