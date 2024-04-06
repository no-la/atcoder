from collections import deque
import sys
# set:再帰回数上限値の指定／引数にはPythonインタープリタのスタックの深さを指定する
sys.setrecursionlimit(1300000)
H, W = map(int, input().split())
A = [list(input()) for _ in range(H)]
start = 0
for i in range(H):
    if start:
        break
    for j in range(W):
        if A[i][j]=="S":
            start = (i, j)
            break
        
N = int(input())
for i in range(N):
    r, c, e = map(int, input().split())
    if A[r-1][c-1]!="T":
        A[r-1][c-1] = e

# print(*A, sep="\n")

used = [[False]*W for _ in range(H)]
def f(i, j, e):
    if isinstance(A[i][j], int): # くすり
        e = A[i][j]
        used[i][j] = True
    # print(i, j, e)

    # 周囲の薬を探す
    # BFS
    todo = deque([(i, j, 0)])
    seen = set()
    seen.add((i, j))
    while todo:
        vi, vj, vdist = todo.popleft()
        wdist = vdist + 1
        if wdist>e:
            continue
        for di, dj in [(0, -1),(0, 1),(-1, 0),(1, 0)]:
            wi, wj = (vi+di, vj+dj)
            if not (0<=wi<H and 0<=wj<W):
                continue
            if (wi, wj) in seen: # 既に調べた点は飛ばす
                continue
            if A[wi][wj]=="#":
                continue
            if A[wi][wj]=="T":
                # print("from", i, j, e)
                print("Yes")
                exit()
            if isinstance(A[wi][wj], int) and not used[wi][wj]: # 薬なら再帰
                f(wi, wj, e-wdist)
            else:
                todo.append((wi, wj, wdist))
            seen.add((wi, wj))
                
    # 再帰で戻るときの処理
    used[i][j] = False
    # print("back")
    # print(*["".join(["*" if (i, j) in seen else "." for j in range(W)]) for i in range(H)], sep="\n")


f(*start, 0)
print("No")