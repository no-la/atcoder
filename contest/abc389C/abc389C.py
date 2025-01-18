Q = int(input())

ans = []
d = [0]
offset = 0
offset_i = 0
for _ in range(Q):
    t, *others = map(int, input().split())
    if t == 1:
        l = others[0]
        d.append(d[-1] + l)
    elif t == 2:
        offset_i += 1
        offset = d[offset_i]
    else:
        k = others[0]
        temp = d[k - 1 + offset_i] - offset
        ans.append(temp)

print(*ans, sep="\n")
