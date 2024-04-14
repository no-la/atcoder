S = input()
from collections import defaultdict
d = defaultdict(int)
for s in S:
    d[s]+=1
# print(d)
e = [0]*1000
for v in d.values():
    e[v] += 1
print("Yes" if all([i==0 or i==2 for i in e]) else "No")