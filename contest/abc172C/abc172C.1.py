N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

DA = [0]*(N+1) # DA[i]: Aの[0, i)を読むのにかかる時間
DB = [0]*(M+1) # DB[i]: Bの[0, i)を読むのにかかる時間
for i in range(1, N+1):
    DA[i] = DA[i-1] + A[i-1]
for i in range(1, M+1):
    DB[i] = DB[i-1] + B[i-1]

import bisect
#基本的にbisect_leftを使う
#渡す配列は昇順(reverse=False)ソートしておく
ans = 0
for i in range(N+1):
    if DA[i]>K:
        break
    ans = max(ans, i + bisect.bisect_right(DB, K-DA[i]) - 1)
print(ans)