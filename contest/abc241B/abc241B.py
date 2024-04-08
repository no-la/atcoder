N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for i in range(M):
    for j in range(N):
        if B[i]==A[j]:
            A[j] = -1
            break
    else:
        print("No")
        exit()
print("Yes")