N, Q = map(int, input().split())

d = set()
for _ in range(Q):
    t, a, b = map(int, input().split())
    if t == 1:
        d.add((a, b))
    elif t == 2:
        d.discard((a, b))
    else:
        print("Yes" if (a, b) in d and (b, a) in d else "No")
