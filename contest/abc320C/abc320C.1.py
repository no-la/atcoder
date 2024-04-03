N = 3
M = int(input())
S = [list(map(int, input())) for _ in range(N)]

INF = N*M+100
# 全探索
# O(M^N) < 10^6
ans = INF
for i in range(10):
    t = 0
    selected = [False]*N
    while (not all(selected)) and t<=N*M: # N周してだめなら揃わない
        for j in range(N):
            if (not selected[j]) and S[j][t%M]==i:
                selected[j] = True
                break
        t += 1
    if all(selected):
        # print("ans", i, ans, t-1)
        ans = min(ans, t-1)

print(ans if ans!=INF else -1)