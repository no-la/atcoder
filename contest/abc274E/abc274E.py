import itertools

N, M = map(int, input().split())
town = [tuple(map(int, input().split())) for _ in range(N)]
booster = [tuple(map(int, input().split())) for _ in range(M)]

INF = 10**15

dp = [
    [[[INF] * (M + 1) for _ in range(N + M)] for _ in range(2**M)] for _ in range(2**N)
]
# dp[s][t][i][j]: 訪れた街の集合s, 訪れた宝箱t, 最後にいる場所i, 取ったブースターの個数jに対して、最小の時間
# iはi<Nなら街i, i>=Nなら宝箱i-N

for sk in range(N + 1):
    # 重複なし組み合わせ O(nCk)
    for sl in itertools.combinations(range(N), sk):
        s = set(sl)
        for tk in range(M + 1):
            for tl in itertools.combinations(range(M), tk):
                t = set(tl)
                for i in range(N + M):
                    for j in range(M + 1):
                        # 配る
                        # 街へ
                        for ni in range(N):
                            if ni in s:
                                continue
                        # 宝箱へ
                        for nik in range(M):
                            ni = N + nik
                            if ni in t:
                                continue
                            nj = j + 1
                            dp[s][t + set([i])][ni][nj] = min(
                                dp[s][t + set([i])][ni][nj], dp[s][t][i][j] + ...
                            )
                            ...
