"""WA"""

N, X = map(int, input().split())
d = [list(map(int, input().split())) for _ in range(N)]


l, r = 0, 10**10
while l + 1 < r:  # lは達成できる、rは達成できない
    c = (l + r) // 2
    remain = X
    for a, p, b, q in d:
        # c個分処理するための最小コストを求める
        min_cost = 10**10
        if p * b > q * a:
            a, p, b, q = b, q, a, p
        # aの方がコスパ良し
        base, need = divmod(c, a * b)
        base *= b
        # aで全探索
        for i in range(b):
            b_count = max(0, -(-(need - i * a) // b))
            min_cost = min(min_cost, (base + i) * p + b_count * q)
        # bで全探索
        for i in range(a):
            a_count = max(0, -(-(need - i * b) // a))
            min_cost = min(min_cost, (base + a_count) * p + i * q)

        remain -= min_cost
        if remain < 0:
            break
    else:
        l = c
        continue
    r = c

print(l)
