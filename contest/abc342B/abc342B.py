N = int(input())
P = list(map(int, input().split()))
D = [-1]*(N+1)
for i in range(N):
    D[P[i]] = i
    
Q = int(input())
for _ in range(Q):
    a, b = map(int, input().split())
    print(a if D[a]<D[b] else b)