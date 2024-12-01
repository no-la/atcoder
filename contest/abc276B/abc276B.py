N, M = map(int, input().split())

d = [[] for _ in range(N)]
# d[i]: iから行ける都市のlist

for _ in range(M):
    a, b = map(lambda x: int(x) - 1, input().split())
    d[a].append(b)
    d[b].append(a)

for i in range(N):
    print(len(d[i]), *[a + 1 for a in sorted(d[i])])
