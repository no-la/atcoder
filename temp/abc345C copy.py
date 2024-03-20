S = input()
N = len(S)

d = {s:[0]*(N+1) for s in "abcdefghijklmnopqrstuvwxyz"} # d[s][i]: 文字sがi番目までに出てくる回数
b = False
for i in range(1, N+1):
    for s in "abcdefghijklmnopqrstuvwxyz":
        d[s][i] = d[s][i-1]
    d[S[i-1]][i] += 1
ans = 0
for i in range(N):
    # 自分より後に出てくる文字との入れ替えを数える
    ans += N-1-i  - (d[S[i]][-1]-d[S[i]][i+1])

if any([v[-1]>=2 for v in d.values()]):
    ans += 1
print(ans)