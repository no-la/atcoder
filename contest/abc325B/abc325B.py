N = int(input())
WX = [list(map(int, input().split())) for i in range(N)]

ans = [0]*24
for t in range(24):
    for wx in WX:
        if 9 <= (wx[1]+t)%24 < 18:
            ans[t] += wx[0]

print(max(ans))