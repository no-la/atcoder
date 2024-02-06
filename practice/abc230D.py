N, D = map(int, input().split())
LR = [tuple(map(int, input().split())) for _ in range(N)]

LR.sort(key=lambda x:x[1]) #Rでソート

ans = 0
i = 0
br = -1
while i<N:
    if LR[i][0]<=br:
        i += 1
        continue
    br = LR[i][1] + D -1
    ans += 1
    i += 1
print(ans)