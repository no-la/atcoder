Q = int(input())
MOD = 998244353

S = [1]
i = 0
ans = 1
for _ in range(Q):
    l = list(map(int, input().split()))
    if l[0]==1:
        x = l[1]
        S.append(x)
        ans *= 10
        ans += x
        ans %= MOD
    elif l[0]==2:
        ans -= S[i]*pow(10, len(S)-i-1, MOD)
        ans %= MOD
        i += 1
    else:
        print(ans)
