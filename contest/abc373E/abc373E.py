import bisect

N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = sorted(A)
cumsum = [0] * (N + 1)
for i in range(N):
    cumsum[i + 1] = cumsum[i] + B[i]

if N == M:
    print(*[0] * N, sep=" ")
    exit()
L = K - sum(A)
ans = []
# print(L)
# print(B)

for i, a in enumerate(A):
    if N - bisect.bisect_right(B, a + L) >= M:
        ans.append(-1)
        continue
    l, r = -1, L
    while l < r - 1:  # (l, r]が条件を満たす
        c = (l + r) // 2
        ge_i = bisect.bisect_right(B, a + c)  # 既にcより大きいのがN-ge_i人いる
        need_count = M - (N - ge_i)  # need_count人だけa+cを越せば当選しない
        if B[ge_i - 1] == a:
            need_vote = (a + c + 1) * need_count - (
                cumsum[ge_i - 1] - cumsum[ge_i - 1 - need_count]
            )  # 必要な票数はneed_vote
        else:
            need_vote = (a + c + 1) * need_count - (
                cumsum[ge_i] - cumsum[ge_i - need_count]
            )  # 必要な票数はneed_vote
        # print(
        # i,
        # a,
        # f"{l=}, {r=}, {c=}, {ge_i=}, {need_count=}, {need_vote=}, remain={L-c}",
        # )
        if need_vote <= L - c:
            l = c
        else:
            r = c
    ans.append(r)

print(*ans, sep=" ")
