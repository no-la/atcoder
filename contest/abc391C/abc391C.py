N, Q = map(int, input().split())

count = [1] * N
at = list(range(N))
ans = 0

for _ in range(Q):
    t, *others = map(int, input().split())
    if t == 1:
        p, h = others
        p -= 1
        h -= 1
        before_h = at[p]
        count[before_h] -= 1
        at[p] = h
        count[h] += 1

        if count[before_h] == 1:
            ans -= 1
        if count[h] == 2:
            ans += 1
    else:
        print(ans)
