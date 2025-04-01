import sys

input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(N)]
MB = max(AB, key=lambda x: x[1])[1]


AB.sort()

ans = 1
imos = [0] * (MB + 1)
r = 0
for l in range(N):
    while r < N and AB[r][0] <= AB[l][0] + K:
        imos[AB[r][1]] += 1
        if AB[r][1] + K + 1 <= MB:
            imos[AB[r][1] + K + 1] -= 1
        r += 1

    restored_imos = [0] * (MB + 1)
    # restored_imos[i]: 体重i以下の人数
    for i in range(MB):
        restored_imos[i + 1] = restored_imos[i] + imos[i + 1]

    ans = max(ans, *restored_imos)

    # l を +1 する準備
    imos[AB[l][1]] -= 1
    if AB[l][1] + K + 1 <= MB:
        imos[AB[l][1] + K + 1] += 1

print(ans)
