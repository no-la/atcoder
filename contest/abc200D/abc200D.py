N = int(input())
MOD = 200
A = list(map(lambda x: int(x)%MOD, input().split()))

dp = [[0]*MOD for _ in range(N)]
# dp[i][s]: 末項A[i]、和sの部分列の個数
# init
for i in range(N):
    dp[i][A[i]] = 1


for i in range(1, N):
    for s in range(MOD):
        for j in range(i):
            dp[i][s] += dp[j][(s-A[i])%MOD]

# print(*dp, sep="\n")

for s in range(MOD):
    count = 0
    tar = []
    for i in range(N):
        if dp[i][s]:
            count += dp[i][s]
            tar.append(i)
            if count>=2:
                break
    if count>=2:
        break

# print(s, tar, count)
if count<2:
    print("No")
    exit()


# B, Cを作る
S = s
B = [tar[0]]
C = [tar[-1]]
bs = (S-A[B[0]])%MOD
cs = (S-A[C[0]])%MOD
while bs!=0:
    i = B[-1]
    for j in range(i):
        if dp[j][bs]>=1:
            B.append(j)
            bs -= A[j]
            bs %= MOD
        
while cs!=0:
    i = C[-1]
    for j in range(i):
        if dp[j][cs]>=1:
            C.append(j)
            cs -= A[j]
            cs %= MOD

if B==C:
    1/0
print("Yes")
print(len(B), *list(map(lambda x: x+1, B[::-1])))
print(len(C), *list(map(lambda x: x+1, C[::-1])))
