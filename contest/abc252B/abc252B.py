N, K = map(int, input().split())
A = list(map(int, input().split()))
B = set(map(int, input().split()))

m = max(A)
for i in range(N):
    a = A[i]
    if i+1 in B and a==m:
        print("Yes")
        exit()

print("No")
