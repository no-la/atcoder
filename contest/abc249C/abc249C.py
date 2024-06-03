N, K = map(int, input().split())
S = [input() for _ in range(N)]

# 全探索？
# 2^15 * 26

ans = 0
# bit全探索
for i in range(2 ** N):
    count = {s:0 for s in "abcdefghijklmnopqrstuvwxyz"}
    for j in range(N):
        if not ((i >> j) & 1):
            continue
        # S[j]を選ぶ
        for s in S[j]:
            count[s] += 1
    ans = max(ans, sum([v==K for v in count.values()]))

print(ans)
