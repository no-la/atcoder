N, M, *S = map(int, input().split())
homes = [tuple(map(int, input().split())) for _ in range(N)]

from collections import defaultdict

dh = defaultdict(list)
route = [S]
for _ in range(M):
    D, C = input().split()
    C = int(C)
    s = D
    if s == "L":
        delta = (-1, 0)
    elif s == "R":
        delta = (1, 0)
    elif s == "U":
        delta = (0, 1)
    elif s == "D":
        delta = (0, -1)

    route.append([route[-1][0] + delta[0] * C, route[-1][1] + delta[1] * C])

ans = 0
for x, y in homes:
    for i in range(1, len(route)):
        x1, y1 = route[i - 1]
        x2, y2 = route[i]
        if x1 == x2:
            if x1 == x and min(y1, y2) <= y <= max(y1, y2):
                ans += 1
        else:
            if y1 == y2 and y1 == y and min(x1, x2) <= x <= max(x1, x2):
                ans += 1

print(ans)
