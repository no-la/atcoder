import math

N = int(input())
d = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)] + [[0, 0]]

ans = 0
for i in range(len(d) - 1):
    ni = i + 1
    ans += math.sqrt((d[i][0] - d[ni][0]) ** 2 + (d[i][1] - d[ni][1]) ** 2)

print(ans)
