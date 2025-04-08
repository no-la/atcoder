import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
W = list(map(int, input().split()))
B = list(map(int, input().split()))
M = max(W)  # ~ 50
K = max(B) + M * (M + 1) // 2  # ~ 7*10^4

INF = 10**18

Grundy = [[INF] * (K + 1) for _ in range(M + 1)]
# Grundy[i][j]: N=1、白i個、青j個のときのGrundy数

for i in range(M + 1):
    for j in range(K + 1):
        # MEXの計算
        exists = set()
        if i >= 1 and j + i <= K:
            exists.add(Grundy[i - 1][j + i])
        for k in range(1, j // 2 + 1):
            exists.add(Grundy[i][j - k])

        for x in range(K + 1):  # O(j)以下で抜けるはず
            if x not in exists:
                Grundy[i][j] = x
                break

# print(*Grundy, sep="\n")

ans = 0
for i in range(N):
    ans ^= Grundy[W[i]][B[i]]
    # print(W[i], B[i], "->", Grundy[W[i]][B[i]], ans)

print("First" if ans else "Second")
