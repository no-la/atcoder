N = int(input())
A = list(map(int, input().split()))

d = [[] for _ in range(2)]
# d: パリティごとに降順

for a in A:
    d[a % 2].append(a)

ans = -1
for i in range(2):
    if len(d[i]) >= 2:
        d[i].sort(reverse=True)
        ans = max(ans, d[i][0] + d[i][1])

print(ans)
