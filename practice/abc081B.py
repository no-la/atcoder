N = int(input())
A = list(map(int, input().split()))

for i in range(31):
    for j in range(N):
        if A[j]%2 != 0:
            print(i)
            exit()
    else:
        for j in range(N):
            A[j] /= 2
