for t in range(1, 11):
    # t = 1
    N = int(input())
    bd = list(map(int, input().split()))
    tot = 0
    for i in range(2, N-2):
        res = bd[i] - max(bd[i-2], bd[i-1], bd[i+1], bd[i+2])
        tot = tot + res if res > 0 else tot
    print(f"#{t} {tot}")