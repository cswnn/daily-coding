from collections import deque
def solution(begin, target, words):
    answer = 0
    
    # begin -> target 최소 필요 단어 변환 횟수 리턴 -> bfs
    # 변환 불가 시 0 리턴
    
    words = {word: 0 for word in words}
    
    if target not in words:
        return 0
    
    def bfs():
        words[begin] = 1
        queue = deque([begin])

        while queue:
            pw = queue.popleft()

            # words 단어들 중 현재 단어(pw)로 만들 수 있는 단어 queue에 추가
            for nw in words:
                if words[nw]: continue # 이미 했던 단어 제외
                cnt = 0
                
                # 두 단어 알파벳 비교
                for i, j in zip(pw, nw): 
                    if i != j:
                        cnt += 1

                # 알파벳 2개 이상 다른 단어 제외
                if cnt > 1: 
                    continue
                # 알파벳 1개만 다른 단어    
                else: 
                    if nw == target:
                        answer = words[pw] + 1 - 1 # 1로 시작했으므로
                        print(nw, answer)
                        return answer
                    words[nw] = words[pw] + 1
                    queue.append(nw)
    
    answer = bfs()
    
    return answer