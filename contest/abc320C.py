m = int(input())
s = [input(), input(), input()]

ans = []
for a in range(10):
    b = str(a)
    s_b_index = [[int(i) for i, e in enumerate(list(j)) if e==b] for j in s]
    for x in range(3):
        temp = s_b_index[x].copy()
        for j in temp:
            s_b_index[x].append(j+m)
            s_b_index[x].append(j+2*m)
    # print(s_b_index)

    for i in range(3*m):
        pass
        