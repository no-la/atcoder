N, M = map(int, input().split())
X, Y = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0
now = 0
ai = 0
bi = 0
while ai<N and bi<M:
    from_a, from_b = False, False
    while ai<N:
        if now<=A[ai]:
            now = A[ai]+X
            from_a = True
            break
        ai += 1
    while bi<M:
        if now<=B[bi]:
            now = B[bi]+Y
            from_b = True
            break
        bi += 1
    if from_a and from_b:
        ans += 1

print(ans)