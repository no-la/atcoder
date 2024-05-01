N = int(input())
S = input()
Q = int(input())

# imos法
imos = [0]*(2*N)
#始点に+x, 終点の次の点に-xする
for _ in range(Q):
    t, a, b = map(int, input().split())
    a -= 1
    b -= 1
    if t==1:
        imos[a] += b-a
        if a+1<2*N:
            imos[a+1] -= b-a
        imos[b] += a-b
        if b+1<2*N:
            imos[b+1] -= a-b
    else:
        imos[0] += N
        imos[N] -= N
        imos[N] -= N
# 適当な処理
for i in range(1, len(imos)):
    imos[i] += imos[i-1]


ans = []
for i in range(2*N):
    ans.append(S[i+imos[i]])
print("".join(ans))
