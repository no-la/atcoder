N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

c = 0
ai, bi = 0, 0
for i in range(N+M+1):
    if ai<N and c+A[ai]<=K and (bi==M or A[ai]<B[bi]):
        c += A[ai]
        ai += 1
    elif bi<M and c+B[bi]<=K:
        c += B[bi]
        bi += 1
    else:
        break
    

print(i)