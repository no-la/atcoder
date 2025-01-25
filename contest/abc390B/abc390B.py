N = int(input())
A = list(map(int, input().split()))

for i in range(N - 1):
    if A[1] * A[i] != A[i + 1] * A[0]:
        print("No")
        exit()

print("Yes")
