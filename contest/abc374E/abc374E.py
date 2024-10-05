"""NS"""

N, X = map(int, input().split())
d = [list(map(int, input().split())) for _ in range(N)]

l, r = 0, 10**10
while l + 1 < r:  # lは達成できる、rは達成できない
    c = (l + r) // 2
    remain = X
    for a, p, b, q in d:
        # c個分処理するための最小コストを求める

        min_cost = ...
        remain -= min_cost
        if remain < 0:
            break
    else:
        l = c
        continue
    r = c

print(l)
