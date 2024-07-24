N, K = map(int, input().split())
A = list(map(int, input().split()))

d = [sorted(A[i::K]) for i in range(min(K, N))]

for i in range(1, N):
    ni, nj = divmod(i, K)
    pi, pj = divmod(i-1, K)
    if d[nj][ni]<d[pj][pi]:
        print("No")
        exit()

print("Yes")
