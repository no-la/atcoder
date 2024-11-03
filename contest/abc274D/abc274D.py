N, X, Y = map(int, input().split())
A = list(map(int, input().split()))
M = 10**4

AX = A[::2]
AY = A[1::2]

from collections import defaultdict

dpx = [defaultdict(lambda: False) for _ in range(N)]
dpy = [defaultdict(lambda: False) for _ in range(N)]
dpx[0][0] = True
dpx[1][AX[0]] = True
dpy[0][0] = True

for i, a in enumerate(AX):
    if i == 0:
        continue
    for x in dpx[i].keys():
        dpx[i + 1][x + a] = True
        dpx[i + 1][x - a] = True
for i, a in enumerate(AY):
    for y in dpy[i].keys():
        dpy[i + 1][y + a] = True
        dpy[i + 1][y - a] = True

# print(*dpx, "-" * 20, sep="\n")
# print(*dpy, sep="\n")
print("Yes" if dpx[len(AX)][X] and dpy[len(AY)][Y] else "No")
