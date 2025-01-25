A = list(map(int, input().split()))

for i in range(len(A) - 1):
    if A[i] > A[i + 1]:
        A[i], A[i + 1] = A[i + 1], A[i]
        break
else:
    print("No")
    exit()


print("Yes" if A == sorted(A) else "No")
