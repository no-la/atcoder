import bisect

H, W, *s = map(int, input().split())
hw = [H, W]

from collections import defaultdict

N = int(input())
wall = [defaultdict(list), defaultdict(list)]
for _ in range(N):
    r, c = map(lambda x: int(x) - 1, input().split())
    wall[0][r].append(c)
    wall[1][c].append(r)
for k in range(2):
    for i in wall[k].keys():
        wall[k][i].sort()

# print(*wall[0], "-" * 20, sep="\n")
# print(*wall[1], "-" * 20, sep="\n")

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
        to_max_i = bisect.bisect_left(wall[k][pos[k]], pos[k ^ 1])
        direction = 1
    else:
        to_max_i = bisect.bisect_left(wall[k][pos[k]], pos[k ^ 1]) - 1
        direction = -1

    if 0 <= to_max_i < len(wall[k][pos[k]]):
        to_max = wall[k][pos[k]][to_max_i] - direction
    else:
        if direction == -1:
            to_max = 0
        else:
            to_max = hw[k ^ 1] - 1

    # print(
    #     pos,
    #     d,
    #     l,
    #     to_max,
    #     to_max_i,
    #     (direction * (pos[k ^ 1] + direction * l), direction * to_max),
    # )

    if direction * (pos[k ^ 1] + direction * l) < direction * to_max:
        pos[k ^ 1] += direction * l
    else:
        pos[k ^ 1] = to_max

    # pos[0] = max(0, min(pos[0], H - 1))
    # pos[1] = max(0, min(pos[1], W - 1))

    print(*list(map(lambda x: int(x) + 1, pos)))
