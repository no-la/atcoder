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
bs = A[B[0]]
cs = A[C[0]]

j = B[0]-1
while j>=0:
    if dp[j][S-bs]>0:
        B.append(j)
        bs += A[j]
        bs %= MOD
    j -= 1

while cs!=S:
    for j in range(C[-1]):
        if dp[j][S-cs]>0:
            C.append(j)
            cs += A[j]
            cs %= MOD
            break

print("Yes")
print(len(B), *list(map(lambda x: x+1, B[::-1])))
print(len(C), *list(map(lambda x: x+1, C[::-1])))
