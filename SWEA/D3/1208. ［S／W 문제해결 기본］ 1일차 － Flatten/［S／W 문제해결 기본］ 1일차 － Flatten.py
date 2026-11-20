# 5215
# 주어진 재료를 갖고 제한 칼로리를 넘지 않는 최대 맛 햄버거 리턴

# from itertools import combinations

# # 테스트 케이스
# # T = int(input())
# T = 1

# # def dfs():
# #     if tot < max_cal

# for test_case in range(1, T+1):
#     # 재료의 수, 제한 칼로리 (N <= 20)
#     # N, L = map(int, input().split())
#     N, L = 5, 1000
#     max_sum = 0

#     # N개의 줄: 재료의 맛, 재료의 칼로리
#     # ingrd = []
#     # for _ in range(N):
#     #     t, k = map(int, input().split())
#     #     ingrd.append((t, k))
#     ingrd = [(100, 200), (300, 500), (250, 300), (500, 1000), (400, 400)]

#     for i in range(1, N+1):
#         for lst in combinations(ingrd, i):
#             s = sum(x[1] for x in lst)
#             if s <= L:
#                 max_sum = max(max_sum, sum(x[0] for x in lst))



#     print(f"#{test_case} {max_sum}")

# 1208
T = 10
for test_cases in range(1, T+1):
    dump = int(input())
    boxes = list(map(int, input().split()))

    for _ in range(dump):
        max_v = max(boxes)
        min_v = min(boxes)
        for i, v in enumerate(boxes):
            if v == max_v:
                boxes[i] -= 1
                for j, m in enumerate(boxes):
                    if m == min_v:
                        boxes[j] += 1
                        break
                break

    res = max(boxes) - min(boxes)

    print(f"#{test_cases} {res}")