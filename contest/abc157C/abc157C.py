N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(M)]

for n in range(10**N):
    ns = str(n)
    if not len(ns)==N:
        continue
    for s, c in A:
        if ns[s-1]!=str(c):
            break
    else:
        print(ns)
        exit()

print(-1)