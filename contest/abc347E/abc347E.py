N, Q = map(int, input().split())
X = list(map(lambda x: int(x)-1, input().split()))
A = [0]*N
S = [None]*N # # S[i]: 整数iがSに入ったクエリの番目
NS = 0
e = [0] # e[i]: 各クエリで、Sに挿入、取り出し後のlen(S)の累積和

# 何クエリ分Sに入っていたかを記録して、出るときにA[j]にたす
for i in range(Q):
    if S[X[i]]==None:
        S[X[i]] = i
        NS += 1
    else:
        A[X[i]] += e[i] - e[S[X[i]]]
        S[X[i]] = None
        NS -= 1
    e.append(NS+e[-1])
# 残った分
for x in range(N):
    if S[x]==None:
        continue
    A[x] += e[-1] - e[S[x]]
    S[x] = None
print(*A)