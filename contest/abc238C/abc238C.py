N = int(input())
MOD = 998244353

ans = -1 # 0の分だけ除く
for i in range(1, 20):
    l = 10**(i-1)
    k = l*10
    if N<k-1:
        ans = (ans + 1+l)%MOD
    else:
        ans = (ans + 9*l*(9*l+1))//2%MOD
print(ans%MOD)
