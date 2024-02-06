N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

#3点が同一直線上になければ良い
#300C3~4*10^6
import math
def get_vec(i, j):
    s = (A[i][0]-A[j][0], A[i][1]-A[j][1])
    if s[0]==0 and s[1]==0:
        return (0, 0)
    elif s[0]==0:
        return (0, 1)
    elif s[1]==0:
        return (1, 0)
    else:
        g = math.gcd(s[0], s[1])
        g = abs(g)*(s[0]/abs(s[0]))
        return (s[0]/g, s[1]/g)

ans = 0
for i in range(N):
    for j in range(i, N):
        s = get_vec(i, j)
        if s==(0, 0):
            continue
        for k in range(j, N):
            t = get_vec(i, k)
            if s!=t:
                ans += 1
print(ans)