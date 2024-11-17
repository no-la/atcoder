import bisect

H, W, *s = map(int, input().split())
hw = [H, W]

N = int(input())
wall = [[[] for _ in range(k)] for k in hw]
for _ in range(N):
    r, c = map(lambda x: int(x) - 1, input().split())
    wall[0][r].append(c)
    wall[1][c].append(r)
for k in range(2):
    for i in range(hw[k]):
        wall[k][i].sort()

Q = int(input())
pos = list(map(lambda x: x - 1, s))
for _ in range(Q):
    d, l = input().split()
    l = int(l)
    if d in ["L", "R"]:
        k = 0
    else:
        k = 1

    if d in ["D", "R"]:
        to_max_i = bisect.bisect_left(wall[k][pos[k ^ 1]], pos[k]) + 1
        direction = 1
    else:
        to_max_i = bisect.bisect_left(wall[k][pos[k ^ 1]], pos[k]) + 1
        direction = -1

    if 0 <= to_max_i < hw[k]:
        to_max = wall[k][pos[k ^ 1]][to_max_i]
    else:
        if direction == -1:
            to_max = 0
        else:
            to_max = hw[k] - 1

    if direction * pos[k] < direction * to_max:
        pos[k] += direction * l
    else:
        pos[k] = to_max

    print(pos)

print(pos)
