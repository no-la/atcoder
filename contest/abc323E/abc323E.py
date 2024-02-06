N, X = map(int, input().split())
T = list(map(int, input().split()))
mod = 998244353
n_1 = pow(N, -1, mod)

#動的計画法
ans = [1] #i秒に曲の再生が止まる確率
for i in range(1, X+1):
    ans.append(0)
    for j in range(N):
        v = i-T[j]
        if v<0:
            continue
        else:
            ans[i] = (ans[i]+ans[v]*n_1)%mod

#(X-T[0]+1)~X秒の間に曲が止まる確率（それぞれ互いに背反）→この間に止まって曲1が再生されればよい
p = 0
for i in range(X-T[0]+1, X+1):
    if i<0:
        continue
    p += ans[i]

print(p*n_1%mod)