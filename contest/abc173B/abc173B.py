N = int(input())
from collections import defaultdict
d = defaultdict(int)
for _ in range(N):
    d[input()] += 1

print(*[f"{s} x {d[s]}" for s in ["AC", "WA", "TLE", "RE"]], sep="\n")