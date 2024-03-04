n, k = map(int, input().split())
MOD = 10**9 + 7

def c(s, t):
    # sCt
    if s-t<t:
        t = s-t
    u = 1
    for i in range(t):
        u = (u*(s-i)) % MOD
    v = 1
    for i in range(t):
        v = (v*(i+1)) % MOD
    # v'*(sCt) = u', v'~v, u~u' mod MOD -> sCt~?
    # sCt~u*(v^-1)
    # mod MODにおけるvの逆元を求めればよい
    return u*pow(v, -1, MOD) % MOD

if k>=n-1:
    print(c(2*n-1, n)) # nHn
else:
    # print((c(n, k)*c(k+n, n)) % MOD) # nCk * k+1Hn
    print(n*((c(n-1, k)*c(n-1, k-1))%MOD)%MOD)