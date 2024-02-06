N = int(input())
A = list(map(int, input().split()))
B = [-1]*(N+1)
for i in range(N):
    if A[i]==-1:
        ans = [i+1]
    else:
        B[A[i]] = i+1
for i in range(1, N):
    ans.append(B[ans[-1]])

print(" ".join(map(str, ans)))