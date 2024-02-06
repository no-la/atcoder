#TLE!!!!!!!!!!!
import math
N = int(input())
P = list(map(int, input().split()))

def get_rate(bunsi, k):
    rate = 0.9
    bunbo = (1-rate**k)/(1-rate)
    ans = bunsi/bunbo - 1200/math.sqrt(k)
    return ans

#kを固定すれば、RはΣ(0.9)^(k-i)Q_iに比例する まずはこの最大値を調べ、最後にkについてmaxを取る
#r[i][j]:i+1回目までからj+1個選んだときの分子の最大値
bunsi = [[0]*(i+1) for i in range(N)]
bunsi[0][0] = P[0]
for i in range(1, N):
    for j in range(i+1):
        new_rate = P[i] if j==0 else bunsi[i-1][j-1]*0.9+P[i]
        if j==i:
            bunsi[i][j] = new_rate
        else:
            bunsi[i][j] = max(bunsi[i-1][j], new_rate)

#kを動かして最大値を出す
ans = -10000000000
for k in range(N):
    ans = max(ans, get_rate(bunsi[-1][k], k+1))
print(ans)