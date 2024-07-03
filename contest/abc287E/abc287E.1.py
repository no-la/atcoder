N = int(input())
S = [input() for _ in range(N)]

from collections import defaultdict
d = defaultdict(int) # d[s]: sから始まる文字列S_の個数
l = defaultdict(int) # l[s]: sの長さ

# rolling hash っぽい感じで
B = [5, 7]
MOD = [100000007, 998244353]
for s in S:
    rh = [0]*len(B)
    for i in range(len(s)):
        for j in range(len(B)):
            b, mod = B[j], MOD[j]
            rh[j] = rh[j]*b + ord(s[i])
            rh[j] %= mod
        d[tuple(rh)] += 1
        l[tuple(rh)] = i+1
for s in S:
    ans = 0
    rh = [0]*len(B)
    for i in range(len(s)):
        for j in range(len(B)):
            b, mod = B[j], MOD[j]
            rh[j] = rh[j]*b + ord(s[i])
            rh[j] %= mod
        if d[tuple(rh)]>=2:
            ans = max(ans, l[tuple(rh)])
    print(ans)
