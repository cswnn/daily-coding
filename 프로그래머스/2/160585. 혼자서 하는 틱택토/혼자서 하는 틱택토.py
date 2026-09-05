def solution(board):
    answer = -1
    
    # 진행 중인 게임판을 보고 중간에 문제가 있었으면 0, 아니면 1 리턴
    # 선공 O, 빈칸은 dot(.)
    
    # ======= 문제가 있는 경우 =======
    # O 개수 - X 개수 > 2인 경우: O가 연속 2번 놓음
    # O 개수 - X 개수 < 0인 경우: X가 연속 2번 놓음(O가 선공이므로 불가능)
    # X, O 둘 다 이긴 경우
    # X가 이겼는데 {O개수 != X개수}인 경우
    # O가 이겼는데 {O개수 != X + 1개수}인 경우
    # ============================
    
    # 연속 3개 몇개 있는가?(= 누구든 이긴 횟수)
    def win(ch: str):
        cnt = 0
        # 가로 3연속
        for i in board:
            if i[0] == i[1] == i[2] == ch:
                cnt += 1
        
        # 세로 3연속
        for i in range(3):
            if board[0][i] == board[1][i] == board[2][i] == ch:
                cnt += 1
        
        # 대각선 3연속
        if board[0][0] == board[1][1] == board[2][2] == ch:
            cnt += 1
        if board[0][2] == board[1][1] == board[2][0] == ch:
            cnt += 1
            
        return cnt
    
    # O - X 개수 세기
    def cal_ox():
        o, x = 0, 0
        for i in board:
            for j in i:
                if j == 'O':
                    o += 1
                elif j == 'X':
                    x += 1
        
        return o - x
    
    def is_empty():
        for i in board:
            for j in i:
                if j == '.':
                    continue
                else:
                    return 0
        return 1
    
    if is_empty():
        answer = 1
    elif win('O') == win('X') == 1 or not(0 <= cal_ox() < 2):
        answer = 0
    elif (win('O') == 1 and cal_ox() != 1) or\
        (win('X') == 1 and cal_ox() != 0):
        answer = 0
    else:
        answer = 1
    
    return answer