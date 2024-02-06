A, B = map(int, input().split())

l = [0, 1, 2, 4]
for i in l:
    for j in l:
        for k in l:
            if i+j+k == A:
                a = [i, j, k]
            if i+j+k == B:
                b = [i, j, k]

print(sum(set(a)|set(b) - set(a)&set(b)))