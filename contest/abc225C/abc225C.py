N, M = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(N)]
ok = True
#1行目をチェック
if (B[0][0]-1)//7 != (B[0][-1]-1)//7:
    ok = False
for i in range(M-1):
    if B[0][i]+1 != B[0][i+1]:
        ok = False
        break
#各列をチェック
for i in range(1, N):
    for j in range(M):
        if B[i-1][j]+7!=B[i][j]:
            ok = False
            print("No")
            exit()

if ok:
    print("Yes")
else:
    print("No")