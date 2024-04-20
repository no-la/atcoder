N = int(input())
A = list(map(lambda x: int(x)-1, input().split()))
B = [0]*N
for i in range(N):
    B[A[i]] = i

ans = []
for i in range(N):
    if A[i] != i:
        j = B[i] # i <-> j
        ans.append(sorted([i+1, j+1]))
        A[i], A[j] = A[j], A[i]
        B[A[j]] = j
        B[A[i]] = i

print(len(ans))
for a in sorted(ans):
    print(*a)
