N, K = map(int, input().split())
S = input()
MOD = 998244353

count = [0]*(N+1)
for i in range(1, N+1):
    count[i] = count[i-1] + (S[i-1]=="?")
# count[i]: S[:i]にある?の個数
print(count)

ans = 0
temp = 1
for i in range(N-K+1):
    # S[i:i+K]が回文になる場合の数
    c = 0
    s = S[i:i+K]
    for j in range(K):
        if s[j]!="?" and s[-j-1]!="?" and s[j]!=s[-j-1]:
            break
        
    else:
        temp = (temp*count[i+K])
        continue
    