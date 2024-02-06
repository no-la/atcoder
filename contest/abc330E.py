N, Q = map(int, input().split())
L = N+1
A = list(map(int, input().split()))
mex = [0 for _ in range(L)]
for i in A:
    if i < L:
        mex[i] += -1

def search(fr):
    for i in range(fr, L):
        if mex[i] >= 0:
            return i
ans = []
s = search(0)
for _ in range(Q):
    i, x = map(int, input().split())
    if A[i-1] < L:
        mex[A[i-1]] += 1
        if A[i-1]<s and mex[A[i-1]]>=0:
            s = A[i-1]
    if x < L:
        mex[x] -= 1
        s = search(s)
    A[i-1] = x
    ans.append(s)
print("\n".join(map(str, ans)))
