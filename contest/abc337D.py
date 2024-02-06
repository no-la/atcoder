H, W, K = map(int, input().split())
S = [input() for _ in range(H)]
A = [H, W]

def get(b, i, j):
    return S[i][j] if b==0 else S[j][i]

# oを最も多く含む長さKの.o部分文字列を探せばよい
ans = -1
for n in range(2):
    if A[n]<K:
        continue
    for m in range(A[(n+1)%2]):
        # o, xの個数の累積和を出す
        no = [0] #no[i]は、i+1番目の文字より前にあるoの個数
        nx = [0]
        for i in range(A[n]):
            no.append(no[-1])
            nx.append(nx[-1])
            v = get(n, i, m)
            if v=="o":
                no[-1]+=1
            elif v=="x":
                nx[-1]+=1
        # print(no)
        # print(nx)
        #長さKの部分文字列を調べる
        for i in range(K-1, A[n]):
            #S[i-K+1]~S[i]
            if nx[i+1]-nx[i-K+1]==0:
                ans = max(ans, no[i+1]-no[i-K+1])

if ans==-1:
    print(-1)
else:
    print(K-ans)