N = int(input())
A = list(map(int, input().split()))
B = {}
for i in range(N):
    if A[i] not in B:
        B[A[i]] = []
    B[A[i]].append(i)

ans = [-1]*N
s = 0
A.sort(reverse=True)
for i in range(N):
    for j in B[A[i]]:
        if ans[j]!=-1:
            break
        ans[j] = s
    s += A[i]
print(" ".join(map(str, ans)))
    