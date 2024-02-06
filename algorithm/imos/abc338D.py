#https://atcoder.jp/contests/abc338/submissions/49775093
N, M = map(int, input().split())
X = list(map(int, input().split()))

d = [0]*(N+1) #d[i]:橋i+1を切った時に通る島の数
#imos法
for i in range(M-1):
    f, t = sorted((X[i], X[i+1]))
    dt = t-f#0~f, t~Nに+dt, f~t-1に+(N-dt)
    d[1] += dt
    d[f] += -dt+N-dt
    d[t] += dt-N+dt

for i in range(1, N+1):
    d[i] += d[i-1]

print(min(d[1:]))