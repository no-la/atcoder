N, T, M = map(int, input().split())
d = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    d[a].append(b)
    d[b].append(a)


# 全探索行けそうな気がする
# NCT * T^(N-T)
# 10C5 * 5^5 = 252 * 3125 = 787500
# 10C6 * 6^4 = 210 * 1296 = ...
# 10C2 * 2^8 = 45 * 256 = 11520

import itertools

ans = set()
for l in itertools.combinations(range(1, N + 1), T):
    remain = [i for i in range(1, N + 1) if i not in l]
    # print("start", l, remain)
    for k in range(T ** (N - T)):
        teams = [set([a]) for a in l]
        for i in range(N - T):
            j = (k // (T**i)) % T
            for b in d[remain[i]]:
                if b in teams[j]:
                    break
            else:
                teams[j].add(remain[i])
                continue
            break
        else:
            group = [None] * N
            for t in teams:
                ti = min(t)
                for i in list(t):
                    group[i - 1] = ti
            ans.add(tuple(group))
            # print(teams)
            # print(group)

print(len(ans))
