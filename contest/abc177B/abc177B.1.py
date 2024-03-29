S = input()
T = input()
N = len(S)
M = len(T)

ans = 10000
for i in range(N-M+1):
    count = 0
    for j in range(M):
        count += S[i+j]!=T[j]
    ans = min(ans, count)
print(ans)