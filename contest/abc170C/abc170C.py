X, N = map(int, input().split())
P = list(map(int, input().split()))

if X not in P:
    print(X)
    exit()
    
for i in range(1, N+10):
    for j in [-i, i]:
        if X+j not in P:
            print(X+j)
            exit()