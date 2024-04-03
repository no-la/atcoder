N = 3
M = int(input())
S = [list(map(int, input())) for _ in range(N)]

INF = (N+1)*M+100
# 全探索
# O(M^N) < 10^6
ans = INF
for d in range(6):
    for i in range(10):
        selected = [False]*N
        for t in range(INF):
            for jj in range(d//2, d//2+N*((d+1)%2+1), (d+1)%2+1):
                j = jj%N
                if (not selected[j]) and S[j][t%M]==i:
                    selected[j] = True
                    break
            if all(selected):
                # print("ans", i, ans, t)
                ans = min(ans, t)
                break

print(ans if ans!=INF else -1)