def solution(name):
    answer = 0
    
    # 최소 조작으로 name 만들기
    # *최초 글자는 A로만 이루어져 있음 (20자 이하)
    # *반드시 대문자
    # *Z 다음은 A이며 반대도 가능
    
    # 01 각 글자의 최소 조작 횟수 + 02 조작이 필요한 글자로의 최소 이동 횟수
    # 01. 정방향, 역방향 계산해서 최소값.
    for i in name:
        answer += min((ord('Z') - ord(i) + 1), (ord(i) - ord('A')))

    # 02. 꺾을지 말지, 꺾을 거면 언제 꺾을 건지.
    # 꺾는 건 A가 나왔기 때문이므로 그걸 기준으로.
    # 가장 긴 연속된 A 구간을 찾기
#     idx, cnt = 1, 0
#     while idx < n:
#         tmp = 0
#         while idx < n and name[idx] == 'A':
#             tmp += 1
#             idx += 1
#         if idx == n:
#             break
#         cnt = max(cnt, tmp)
#         end = idx # name 중 문자 A가 아닌 마지막 인덱스
#         idx += 1

#     if cnt == 0: # A가 없는 경우
#         answer += n - 1
#     else:
        
    n = len(name)
    min_move = n - 1
    for j in range(n):
        next_idx = j + 1
        while next_idx < n and name[next_idx] == 'A':
            next_idx += 1
        min_move = min(min_move, j * 2 + (n - next_idx), j + (n - next_idx) * 2)
        # 모든 위치에 대해 연속된 A의 정방향/역방향을 고려하므로,
        # 가장 긴 연속된 A를 찾을 필요도 없고, 연속된 A로 name이 종료되는 경우도 일일이 고려할 필요 없음.   
    
    answer += min_move

    return answer