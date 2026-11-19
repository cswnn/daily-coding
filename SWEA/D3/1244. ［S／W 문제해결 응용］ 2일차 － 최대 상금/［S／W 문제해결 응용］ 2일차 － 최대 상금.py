from itertools import combinations
T = int(input())
for t in range(1, T+1):
    n_lst, cnt = map(str, input().split())
    # n_lst, cnt = "928374", "10"
    n_lst = [i for i in n_lst]
    cnt = int(cnt)
    cases = set()
    visited = set()

    change_case = set((i, j) for i, j in combinations([k for k in range(len(n_lst))], 2))

    def dfs(count):
        if count > 0:
            for a, b in change_case:
                n_lst[a], n_lst[b] = n_lst[b], n_lst[a]
                # if int("".join(n_lst)) not in cases:
                    # cases.add(int("".join(n_lst)))
                current_num = "".join(n_lst)
                if (count - 1, current_num) not in visited:
                    visited.add((count - 1, current_num))
                    dfs(count - 1)
                n_lst[a], n_lst[b] = n_lst[b], n_lst[a]

        else:
            cases.add(int("".join(n_lst)))
            return

    dfs(cnt)

    # print(cases)
    print(f"#{t} {max(cases)}")

    # 매번 체크하는 게 아니라 횟수를 모두 끝낸 후 add 해야 함
