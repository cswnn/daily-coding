T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    soil = []
    res = 0
    for i in range(N):
        tmp = str(input())
        tmp = list(map(int, tmp))
        soil.append(tmp)

    for i in range(N):
        for j in range(N):
            if abs(N//2 - i) + abs(N//2 - j) <= N//2:
                res += soil[i][j]

    print(f"#{test_case} {res}")