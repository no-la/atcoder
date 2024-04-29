N, M, K, S, T, X = map(int, input().split())
from collections import defaultdict
d = defaultdict(list)
for _ in range(M):
    u, v = map(int, input().split())
    d[u].append(v)
    d[v].append(u)
MOD = 998244353

dp = [[[0, 0] for j in range(N+1)] for _ in range(K+1)]
ans = 0

# BFS
from collections import deque
todo = deque([(0, S, 0)])
dp[0][S][0] = 1
while todo:
    vi, vj, vk = todo.popleft()
    for w in d[v]:
        wi = vi+1
        wj = w
        wk = (vk + (w==X))%2
        print(wi, wj, wk)
        dp[wi][wj][wk] = (dp[wi][wj][wk] + dp[vi][vj][vk])%MOD
        if wi<K:
            todo.append((wi, wj, wk))

print(dp[K][T][0])

