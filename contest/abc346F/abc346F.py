N = int(input())
S = input()
T = input()

NS = len(S)
NT = len(T)
NNS = N*NS

cs = 97

d = [[-1]*(NT+1) for _ in range(26)] # d[i][j]: j回目にchr(97+i)が出て来るSのインデックス
dmax = [-1]*26
for i in range(26):
    c = 0
    for j in range(NS):
        if S[j]==chr(cs+i):
            c += 1
            d[i][c] = j
    dmax[i] = c

# 決め打ち二分探索
l = 0
r = NNS
while l<r: # [:l]が条件を満たし、[r:]が条件を満たさない
    k = (r+l)//2
    i = 0
    for t in T:
        ti = ord(t) - cs
        if dmax[ti]==0:
            print(0)
            exit()
            
        # ---------------------------------
        # 毎回S[0]スタートではないので、その分ずらす必要がある
        # ---------------------------------
        i += (k//dmax[ti])*NS + d[ti][k%dmax[ti]]
        if i>=NNS:
            # print("i >= NNS")
            break
    else: # kは条件を満たす
        # print(k, chr(ti+cs), i)
        l = k + 1
        continue
    r = k
    # print(k, chr(ti+cs), i)
print(l)