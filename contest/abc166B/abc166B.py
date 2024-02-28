N, K = map(int, input().split())
A = [False]*(N+1)
for i in range(K):
    input()
    l = list(map(int, input().split()))
    for a in l:
        A[a] = True
    
print(A.count(False)-1)