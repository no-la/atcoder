N, P, Q, R = map(int, input().split())
A = list(map(int, input().split()))


# [x, y) -> P
# [x, z) -> P+Q
# [x, w) -> P+Q+R

cumsum = [0]*(N+1) # cumsum[i]: sum(A[:i+1])
for i in range(1, N+1):
    cumsum[i] = cumsum[i-1]+A[i-1]

import bisect
# 基本的にbisect_leftを使う
# 渡す配列は昇順(reverse=False)ソートしておく
for x in range(N):
    tar = cumsum[x]+P
    y = bisect.bisect_left(cumsum, tar)
    
    if y>N or cumsum[y]!=tar:
        continue
    
    tar += Q
    z = bisect.bisect_left(cumsum, tar)
    if z>N or cumsum[z]!=tar:
        continue
    
    tar += R
    w = bisect.bisect_left(cumsum, tar)
    if w>N or cumsum[w]!=tar:
        continue
    
    if 0<=x<y<z<w<=N:
        print("Yes")
        exit()

print("No")
