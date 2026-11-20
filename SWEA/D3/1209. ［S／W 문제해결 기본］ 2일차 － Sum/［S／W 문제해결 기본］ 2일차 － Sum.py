# 1209
# 각 행, 열, 대각선 합 중 최댓값
# 배열의 크기는 100x100
T = 10
size = 100 # 100

for test_case in range(1, T+1):
    _ = input()
    max_v = 0
    lst = []
    for _ in range(size):
        lst.append(list(map(int, input().split())))

    for i in range(size):
        res1 = sum(t[i] for t in lst)
        res2 = sum(lst[i])
        max_v = max(max_v, res1, res2)

    res3 = sum(lst[j][j] for j in range(size))
    res4 = sum(lst[k][size-k-1] for k in range(size))

    max_v = max(max_v, res3, res4)

    print(f"#{test_case} {max_v}")