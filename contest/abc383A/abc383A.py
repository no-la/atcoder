N = int(input())
d = [list(map(int, input().split())) for _ in range(N)]

t = 0
ans = 0
i = 0
while i < N:
    t += 1
    ans = max(0, ans - 1)
    if t == d[i][0]:
        ans += d[i][1]
        i += 1

print(ans)
