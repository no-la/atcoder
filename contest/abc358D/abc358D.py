N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

# 各B[i]に対し、B[i]個以上のお菓子が入った箱の数を調べておくイメージ

import bisect
# 基本的にbisect_leftを使う
# 渡す配列は昇順(reverse=False)ソートしておく
i = 0
ans = 0
for b in B:
    ni = bisect.bisect_left(A, b)
    if i<ni:
        i = ni
    if i>=N:
        print(-1)
        exit()
        
    ans += A[i]
    i += 1

print(ans)
    