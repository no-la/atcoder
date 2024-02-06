N, S, M, L = map(int, input().split())

ans = 10000000000000000000
for s in range(18):
    for m in range(14):
        for l in range(9):
            if 6*s+8*m+12*l >= N:
                ans = min(ans, S*s+M*m+L*l)
print(ans)