N, K = map(int, input().split())
S = input()
MOD = 998244353

count = [0]*(N+1)
for i in range(1, N+1):
    count[i] = count[i-1] + (S[i-1]=="?")
# count[i]: S[:i]にある?の個数
print(count)

