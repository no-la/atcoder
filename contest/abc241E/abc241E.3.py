N, K = map(int, input().split())
A = list(map(int, input().split()))

# X%Nが、N回以下でループする
X = [-1]*(N+1) # X[i]: i回操作時のXの値
c = [None]*(N+1) # c[i]: X[i]%N
X[0] = 0
c[0] = 0
s = [-1]*N # s[i]: c[i]が何回目に出て来るか
s[0] = 0
for i in range(1, N+1):
    X[i] = X[i-1] + A[c[i-1]]
    c[i] = X[i]%N
    if s[c[i]]!=-1: # ループの終点
        start = s[c[i]]
        loop_size = i-start
        loop_value = X[i-1] - X[start-1] # [start, start+loop_size)
        break
    
    s[c[i]] = i

if K<=start:
    print(X[K])
else:
    ans = loop_value*((K-start)//loop_size) + X[start+(K-start)%loop_size-1]
    print(ans)
