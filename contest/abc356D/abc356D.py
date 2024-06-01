N, M = map(int, input().split())
MOD = 998244353

# Mの桁ごとに何回出て来るか調べる
def f(i):
    # i桁目は2^(i+1)回の後半分の2^i回において1になる
    # print(N%(2**(i+1)))
    return (((N//(2**(i+1)))*2**i)%MOD + (max(0, (N%(2**(i+1)))-2**i+1))%MOD)%MOD

ans = 0
for i in range(M.bit_length()):
    if M&(1<<i):
        # print(i, f(i))
        ans = (ans + f(i))%MOD

print(ans)
