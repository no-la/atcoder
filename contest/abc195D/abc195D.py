import bisect
from collections import defaultdict

N, M, Q = map(int, input().split())
INF = 10**6
worthes = [[] for _ in range(INF + 1)]
weights = []
for _ in range(N):
    w, v = map(int, input().split())
    worthes[w].append(v)
    weights.append(w)
weights.sort()
for i in range(INF + 1):
    worthes[i].sort(reverse=True)

X = list(map(int, input().split()))
for _ in range(Q):
    L, R = map(int, input().split())
    count = defaultdict(int)
    ans = 0
    for i, x in enumerate(X):
        if L <= i + 1 <= R:
            continue
        wi = bisect.bisect_right(weights, x) - 1
        w = weights[wi]
        while w > 0 and count[w] >= len(worthes[w]):
            wi -= 1
            w = weights[wi]

        if count[w] < len(worthes[w]):
            ans += worthes[w][count[w]]
            count[w] += 1
        print(w, count, ans)
    print(ans)
