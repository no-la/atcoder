N = int(input())
S = [input() for _ in range(N)]

from collections import defaultdict
d = defaultdict(int)

for s in S:
    print(f"{s}({d[s]})" if d[s] else s)
    d[s] += 1
