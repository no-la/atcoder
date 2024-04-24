N = int(input())
S = [input() for _ in range(N)]
from collections import defaultdict
d = defaultdict(int)
T = set()
for i in range(N):
    d[S[i]] += 1
    T.add(S[i] if S[i][0]!="!" else S[i][1:])

# print(T)
for t in T:
    if d[t]>=1 and d["!"+t]>=1:
        print(t)
        exit()
print("satisfiable")
