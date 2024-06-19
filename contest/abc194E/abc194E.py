N, M = map(int, input().split())
A = list(map(int, input().split()))


# Aの長さMの部分列に対して、そこに含まれない最小の非負整数を考える
# そのうち、最小のものが答え

# 使える数字を持ちながら区間をずらしていく感じ
d = [0]*(N+1) # d[i]: 対称区間にあるiの個数
# 初期化
for i in range(M):
    d[A[i]] += 1

from heapq import heapify, heappop, heappush
di = [i for i in range(N+1) if d[i]==0] # d[di[_]] == 0
heapify(di)
ans = di[0]

for i in range(M, N):
    d[A[i-M]] -= 1
    d[A[i]] += 1
    
    if d[A[i-M]]==0:
        heappush(di, A[i-M])
    
    while d[di[0]]!=0: # diに要素を追加するのがN-M回で、もともとlen(di)<=Nなので、全体でO(2N)
        heappop(di)

    ans = min(ans, di[0])

print(ans)
