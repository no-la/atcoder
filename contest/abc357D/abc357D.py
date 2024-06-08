N = int(input())
MOD = 998244353

M = len(str(N))
K = pow(10, M-1, MOD)

d = [None]*100
# d[i]: i桁目まで

ans = K
i = 1
count = 1
d[1] = K
while count<N:
    while count+2^i>N:
        i -= 1
    count += 2**i
    if d[2**i] is None:
        ans = (ans*pow(10, len(str(ans)), MOD)+ans)%MOD
        d[2**i] = ans
    else:
        ans = (ans*pow(10, len(str(d[2**i])), MOD)+d[2**i])%MOD
    print(i, count, ans)
    i += 1

print(d)

ans = (ans*N)%MOD
print(ans)

