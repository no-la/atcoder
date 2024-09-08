N, M, X, T, D = map(int, input().split())

init = T-X*D
if M<=X:
    print(init+D*M)
else:
    print(init+D*X)
