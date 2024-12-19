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

slash = [i for i in range(N) if S[i] == "/"]

import bisect

for _ in range(Q):
    L, R = map(lambda x: int(x) - 1, input().split())
    l = bisect.bisect_left(slash, L)
    r = bisect.bisect_right(slash, R)
    if l == r:
        print(0)
        continue
    temp = [1]
    while l < r - 1:
        c = (l + r) // 2
        i = slash[c]
        temp.append(min(dl[i] - dl[L], dr[R + 1] - dr[i]) * 2 + 1)
        if dl[i] - dl[L] <= dr[R + 1] - dr[i]:
            l = c
        else:
            r = c
    i = slash[l]
    print(max(temp[-1], min(dl[i] - dl[L], dr[R + 1] - dr[i]) * 2 + 1))
