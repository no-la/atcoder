N, K = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
temp = set()
seen = [False] * N

# できるだけ重複なくK個選ぶ
for i, a in enumerate(A):
    if len(temp) == K:
        break
    temp.add(a)
    seen[i] = True

for i in range(N):
    if len(temp) < K and not seen[i]:
        temp.add(i)
        seen[i] = True

for i in range(N + 1):
    if i not in temp:
        print(i)
        exit()
