N, K = map(int, input().split())
A = list(map(int, input().split()))

# ソートしてN-K要素ずつ見る
A.sort()
ans = 10**15
for i in range(K+1):
    ans = min(ans, A[i+N-K-1]-A[i])

# print(A)
print(ans)
