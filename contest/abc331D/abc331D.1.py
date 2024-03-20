# https://atcoder.jp/contests/abc331/submissions/51468621
N, Q = map(int, input().split())
P = [input() for _ in range(N)]

D = [[0]*(N+1) for _ in range(N+1)] # D[i][j]: [0, i)x[0, j)にあるBlackの個数
for i in range(1, N+1):
    for j in range(1, N+1):
        D[i][j] = D[i-1][j] + D[i][j-1] - D[i-1][j-1] + (P[i-1][j-1]=="B")

def f(a, b):
    """[0, a)x[0, b)にあるBlackの個数"""
    aq, ar = (a//N, a%N) if a%N!=0 else (a//N-1, N) # 0<=ar<Nでなく、0<ar<=Nとする
    bq, br = (b//N, b%N) if b%N!=0 else (b//N-1, N) # 同上
    # NxNで区切る
    # 全部含む部分、右端の部分、下端の部分、右下の部分
    return aq*bq*D[-1][-1] + bq*D[ar][N] + aq*D[N][br] + D[ar][br]

for _ in range(Q):
    a, b, c, d = map(int, input().split())
    c += 1
    d += 1
    # [a, c)x[b, d)にあるBlackの個数を求める
    print(f(c, d) - f(a, d) - f(c, b) + f(a, b))
    