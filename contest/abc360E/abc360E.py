N, K = map(int, input().split())
MOD = 998244353

P = (2*N-2)*pow(N, -2, MOD)%MOD # 黒が動く確率
Q = (N**2-2*N+2)*pow(N, -2, MOD)%MOD # 動かない確率
R = N*(N+1)*pow(2, -1, MOD)%MOD # 1+2+...+N

def f(x):
    return x*Q + P*(R-x)

ans = 1
for _ in range(K):
    ans = f(ans)%MOD

print(ans)
