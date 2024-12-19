N, Q = map(int, input().split())
S = input()

# ある区間の中で、各 "/" の左にある1、右にある2の個数を高速に求めたい
# 累積和でよい
# "/" については二分探索でよさそう

dl = [0] * (N + 1)
dr = [0] * (N + 1)

for i in range(N):
    dl[i + 1] = dl[i] + (S[i] == "1")
    dr[i + 1] = dr[i] + (S[i] == "2")

dr = [dr[-1] - dr[i] for i in range(N + 1)]

# print(dl)
# print(dr)

slash = [i for i in range(N) if S[i] == "/"]

# print(slash)
import bisect

for _ in range(Q):
    L, R = map(lambda x: int(x) - 1, input().split())
    l = bisect.bisect_left(slash, L)
    r = bisect.bisect_right(slash, R)
    # print(L, R, l, r)
    if l == r:
        print(0)
        continue
    ans = 1
    while l < r - 1:
        c = (l + r) // 2
        i = slash[c]
        ans = max(ans, min(dl[i] - dl[L], dr[i] - dr[R + 1]) * 2 + 1)
        if dl[i] - dl[L] <= dr[i] - dr[R + 1]:
            l = c
        else:
            r = c
    i = slash[l]
    ans = max(ans, min(dl[i] - dl[L], dr[i] - dr[R + 1]) * 2 + 1)
    # print(L, i, R)
    print(ans)
