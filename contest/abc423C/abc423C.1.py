import sys

input = lambda: sys.stdin.readline().rstrip()

N, R = map(int, input().split())
L = list(map(int, input().split()))

ans = 0
ml = 100000000
for i in range(R):
    if L[i] == 0:
        ml = i
        break

for i in range(R):
    if i < ml:
        continue
    if L[i] == 0:
        ans += 1
    else:
        ans += 2

mr = -1
for i in range(N - 1, R - 1, -1):
    if L[i] == 0:
        mr = i
        break

for i in range(N - 1, R - 1, -1):
    if i > mr:
        continue
    if L[i] == 0:
        ans += 1
    else:
        ans += 2

print(ans)
