N = int(input())
S = [input() for _ in range(N)]

from collections import defaultdict
d = defaultdict(int)
# d[s]: sから始まる文字列S_の個数
for s in S:
    for i in range(len(s)):
        d[s[:i+1]] += 1

for s in S:
    for i in range(len(s), 0, -1):
        if d[s[:i]]>=2:
            print(i)
            break
    else:
        print(0)

        