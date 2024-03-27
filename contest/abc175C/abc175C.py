X, K, D = map(int, input().split())
X = abs(X)

q, r = divmod(X, D)
if q>=K:
    print(X - D*K)
else:
    print(abs(D*((K-q)%2) - r))
