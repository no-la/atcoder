N, M = map(int, input().split())

d = [0]*M
for _ in range(N):
    k, *A = list(map(int, input().split()))
    for i in range(k):
        d[A[i]-1] += 1
print(d.count(N))