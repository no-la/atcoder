N = int(input())
M = 101
H = [None] * (M**2)
can = [True] * (M**2)

query = []
for _ in range(N):
    x, y, h = map(int, input().split())
    if h == 0:
        query.append((x, y))
        continue
    for k in range(M * M):
        if not can[k]:
            continue
        i, j = divmod(k, M)
        nh = h + abs(i - x) + abs(j - y)
        if H[k] is not None and H[k] != nh:
            can[k] = False
        else:
            H[k] = nh
            can[k] = True

for x, y in query:
    for k in range(M**2):
        i, j = divmod(k, M)
        nh = h + abs(i - x) + abs(j - y)
        if H[k] > nh - h:
            can[k] = False

ans_c = None
ans_h = None
for k in range(M**2):
    if can[k]:
        ans_c = divmod(k, M)
        ans_h = H[k]
        break

print(*ans_c, ans_h, sep=" ")
# print(can.count(True))
