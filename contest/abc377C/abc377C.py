N, M = map(int, input().split())
cannot = set()

for _ in range(M):
    a, b = map(int, input().split())
    cannot.add((a, b))
    for i in [-2, 2]:
        for j in [-1, 1]:
            for k, l in [(a + i, b + j), (a + j, b + i)]:
                if not (1 <= k <= N and 1 <= l <= N):
                    continue
                cannot.add((k, l))

print(N**2 - len(cannot))
# print(cannot)
