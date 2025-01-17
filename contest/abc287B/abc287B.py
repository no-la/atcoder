N, M = map(int, input().split())
S = [input()[-3:] for _ in range(N)]
ans = 0
seen = set()
for _ in range(M):
    t = input()
    if t in seen:
        continue
    seen.add(t)
    ans += S.count(t)

print(ans)
