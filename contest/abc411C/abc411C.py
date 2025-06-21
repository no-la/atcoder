import sys

input = lambda: sys.stdin.readline().rstrip()
N, Q = map(int, input().split())
A = list(map(lambda x: int(x) - 1, input().split()))

d = [0] * N
ans = 0

for a in A:
    d[a] ^= 1
    l = (a - 1 == -1) or (d[a - 1] == 0)
    r = (a + 1 == N) or (d[a + 1] == 0)
    if d[a] == 1:
        if l and r:
            ans += 1
        elif not l and not r:
            ans -= 1
    else:
        if l and r:
            ans -= 1
        elif not l and not r:
            ans += 1

    print(ans)
