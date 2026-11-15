from collections import deque
t = int(input())
for i in range(1, t+1):
    N, M = map(int, input().split())
    lst = map(int, input().split())
    lst = deque(lst)
    for j in range(M):
        lst.append(lst.popleft())
    print(f"#{i} {lst[0]}")
    