X,Y,Z = map(int, input().split())

ans = 0
if abs(X)<abs(Y) or X*Y<0:
    ans = abs(X)
else:
    if abs(Z)<abs(Y) or Z*Y<0:
        ans = abs(Z)+abs(X-Z)
    else:
        ans = -1
print(ans)