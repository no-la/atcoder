N = int(input())
A = list(map(int, input().split()))
Q = int(input())

d = [[0] for _ in range(N+1)] # index
for i in range(N):
    d[A[i]].append(i+1)

# print(*d, sep="\n")
import bisect
# 基本的にbisect_leftを使う
# 渡す配列は昇順(reverse=False)ソートしておく
for _ in range(Q):
    L, R, X = map(int, input().split())
    ri = bisect.bisect_left(d[X], R)
    li = bisect.bisect_left(d[X], L-1)
    print(L, R, d[X], li, ri)
    print(ri-li)
