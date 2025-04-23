import sys

input = lambda: sys.stdin.readline().rstrip()
S = input()
T = input()

from collections import defaultdict

count_s = defaultdict(int)
count_t = defaultdict(int)

for s in S:
    count_s[s] += 1
for t in T:
    count_t[t] += 1


count = 0
for k in "abcdefghijklmnopqrstuvwxyz":
    if k not in "atcoder" and count_s[k] != count_t[k]:
        print("No")
        exit()
    count += abs(count_t[k] - count_s[k])

print("Yes" if count <= count_s["@"] + count_t["@"] else "No")
