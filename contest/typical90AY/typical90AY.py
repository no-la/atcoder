import sys

input = lambda: sys.stdin.readline().rstrip()
N, K, P = map(int, input().split())
TEMP = list(map(int, input().split()))
B = [TEMP[: N // 2], TEMP[N // 2 :]]

d = [[[] for _ in range(len(B[i]) + 1)] for i in range(2)]
# d[i][j]: B[i]のサイズjの部分集合の和のリスト

# bit全探索
for i in range(2):
    M = len(B[i])
    for b in range(2**M):
        s = 0
        for j in range(M):
            if not ((b >> j) & 1):
                continue
            # B[i][j]を選ぶ場合なので、適当な処理を書く
            s += B[i][j]
        d[i][b.bit_count()].append(s)

for i in range(2):
    for j in range(len(d[i])):
        d[i][j].sort()


import bisect

ans = 0
for i, ds in enumerate(d[0]):
    j = K - i
    if j < 0 or j >= len(d[1]):
        continue
    for l in ds:
        ri = bisect.bisect_right(d[1][j], P - l)
        ans += ri
print(ans)
