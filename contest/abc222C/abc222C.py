N, M = map(int, input().split())
A = [input() for _ in range(2*N)]
r = [[0, i] for i in range(2*N)] # r[_]:人[1]の勝利数[0]


d = {"G":0, "C":1, "P":2}
def judge(a, b):
    if a==b:
        return 0, 0
    elif d[a]==(d[b]-1)%3: # aの勝ち
        return 1, 0
    else:
        return 0, 1

for m in range(M):
    for i in range(N):
        a = r[2*i]
        b = r[2*i+1]
        adda, addb = judge(A[a[1]][m], A[b[1]][m])
        a[0] -= adda
        b[0] -= addb
    r.sort()

print("\n".join([str(l[1]+1) for l in r]))