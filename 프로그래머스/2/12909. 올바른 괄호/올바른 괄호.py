def solution(s):
    answer = True
    
    st = []
    for c in s:
        if c == "(":
            st.append(c)
        else:
            if st and st[-1] == "(":
                st.pop()
            else:
                return False
    
    if st:
        return False

    return True