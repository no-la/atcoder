N, Q = map(int, input().split())
d = [list(map(int, input().split()))[1:] for _ in range(N)]

for _ in range(Q):
    s, t = map(int, input().split())
    s -= 1
    t -= 1
    print(d[s][t])
