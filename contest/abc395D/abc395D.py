import sys

input = lambda: sys.stdin.readline().rstrip()
N, Q = map(int, input().split())

# 巣の交換は別で管理

nest = list(range(N))
rnest = list(range(N))
dove = list(range(N))
for _ in range(Q):
    t, *others = map(int, input().split())
    if t == 1:
        a, b = others
        a, b = a - 1, b - 1
        i = rnest[b]
        dove[a] = i
    elif t == 2:
        a, b = others
        a, b = a - 1, b - 1
        i, j = rnest[a], rnest[b]
        k, l = nest[i], nest[j]
        rnest[k], rnest[l] = rnest[l], rnest[k]
        nest[i], nest[j] = nest[j], nest[i]
    else:
        a = others[0] - 1
        print(nest[dove[a]] + 1)
