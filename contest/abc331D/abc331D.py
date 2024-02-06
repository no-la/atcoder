N, Q = map(int, input().split())
P = [input() for _ in range(N)]

data = [[0]*N for _ in range(N)] #各点を右下の頂点にする長方形内のblackの個数

for i in range(N):
    for j in range(N):
        left = 0
        up = 0
        delta = 0
        if 0<i:
            up = data[i-1][j]
        if 0<j:
            left = data[i][j-1]
        if 0<i and 0<j:
            delta = data[i-1][j-1]
        d = 1 if P[i][j]=="B" else 0
        data[i][j] = left+up+d-delta

ans = ""

for _ in range(Q):
    A, B, C, D = map(int, input().split())
    a = A%N
    b = B%N
    c = C%N
    d = D%N
    hor = C//N-A//N-1
    ver = D//N-B//N-1
    contain = 0 if hor==-1 or ver==-1 else min(hor, ver)*data[-1][-1]
    hor_unit = data[-1][-1] + data[c][-1]
    ver_unit = data[-1][-1] + data[-1][d]
    rd = data[c][d]
    ru = data[-1][d]
    ld = data[c][-1]
    lu = data[-1][-1]
    if a>0:
        ru -= data[a-1][d]
        lu -= data[a-1][-1]
        hor_unit -= data[a-1][-1]
    if b>0:
        ld -= data[c][b-1]
        lu -= data[-1][b-1]
        ver_unit -= data[-1][b-1]
    if a>0 and b>0:
        lu += data[a-1][b-1]
    s = ru+rd+contain
    print(ru, rd, ld, lu, contain, ver*ver_unit, hor*hor_unit)
