T = int(input())

for test_case in range(1, T + 1):
  str1 = input()
  str2 = input()

  d = {}

  for i in str1:
    if i not in d:
      d[i] = 0

  for j in str2:
    if j in d:
      d[j] += 1

  max_v = max(d.values())

  print(f"#{test_case} {max_v}")
