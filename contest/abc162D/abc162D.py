N = int(input())
S = input()


def f(s):
    if s=="R":
        return 0
    elif s=="G":
        return 1
    else:
        return 2
    
# 累積和
rgb = [[0]*N,[0]*N,[0]*N]
rgb[f(S[0])][0] = 1

for i in range(1, N):
    for j in range(3):
        rgb[j][i] += rgb[j][i-1]
    rgb[f(S[i])][i] += 1

ans = 0
for i in range(N):
    for j in range(i+1, N):
        if S[i]==S[j]:
            continue
        sk = 3 - (f(S[i])+f(S[j]))
        ans += rgb[sk][N-1]-rgb[sk][j]
        if 2*j-i<N and f(S[2*j-i])==sk:
            ans -= 1
print(ans)
