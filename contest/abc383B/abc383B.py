H, W, D = map(int, input().split())
S = [input() for _ in range(H)]

d = [(i, j) for i in range(H) for j in range(W) if S[i][j] == "."]
ans = 0

# 重複なし組み合わせ O(nCk)
import itertools

for l in itertools.combinations(d, 2):
    hositu = set(l)
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                continue
            for k in range(2):
                if abs(i - l[k][0]) + abs(j - l[k][1]) <= D:
                    hositu.add((i, j))

    ans = max(len(hositu), ans)

print(ans)
