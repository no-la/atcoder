N, D = map(int, input().split())
R = 10**6
L = -R
X = []
Y = []
for _ in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

# 二分探索と累積和
X.sort()
dx = [0]
for x in X:
    dx.append(dx[-1]+x)
Y.sort()
dy = [0]
for y in Y:
    dy.append(dy[-1]+y)


import bisect

# y座標について最小になるようなものを見つけておく
min_y = None
min_v = 10**15
for y in range(L, R+1):
    i = bisect.bisect_left(Y, y)
    v = i*y-dy[i] + (dy[N]-dy[i])-(N-i)*y
    if min_v>v:
        min_v = v
        min_y = y
        
ans = 0
for x in range(L, R+1):
    # xを固定
    i = bisect.bisect_left(X, x)
    value = i*x-dx[i] + (dx[N]-dx[i])-(N-i)*x
    
    # yの範囲を調べる
    if min_v+value>D:
        continue
    
    l, r = min_y, R+1
    while l<r-1: # 条件を満たす最大のlを探す
        y = (l+r)//2
        j = bisect.bisect_left(Y, y)
        temp = j*y-dy[j] + (dy[N]-dy[j])-(N-j)*y

        if value+temp>D:
            r = y
        else:
            l = y
    Ry = r
    
    l, r = L-1, min_y
    while l<r-1: # 条件を満たす最小のrを探す
        y = (l+r)//2
        j = bisect.bisect_left(Y, y)
        temp = j*y-dy[j] + (dy[-1]-dy[j])-(N-j)*y

        if value+temp>D:
            l = y
        else:
            r = y
    Ly = r
    
    ans += Ry-Ly

print(ans)
