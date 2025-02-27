import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

M = 46

da = [0] * M
db = [0] * M
dc = [0] * M
for a, b, c in zip(A, B, C):
    da[a % M] += 1
    db[b % M] += 1
    dc[c % M] += 1

ans = 0
for i in range(46):
    for j in range(46):
        ans += da[i] * db[j] * dc[(46 - i - j) % 46]

print(ans)
