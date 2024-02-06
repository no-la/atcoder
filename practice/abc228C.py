N, K = map(int, input().split())
P = [list(map(int, input().split())) for _ in range(N)]

D = [0]*N #3日の合計点
for i in range(N):
    for j in range(3):
        D[i] += P[i][j]
#3日分の時点でK位の点数を調べる
E = D.copy()
E.sort(reverse=True)
border = 0
for i in range(1, N):
    if E[i]==E[i-1]:
        continue
    if i+1>K: #順位は1、idは0スタート
        border = E[i-1]
        break
# print(border)
for d in D:
    if d+300>=border:
        print("Yes")
    else:
        print("No")