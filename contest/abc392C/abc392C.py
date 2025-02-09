import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

# Q[i]にQ[P[i]]を紐づける
ans = [None] * (N + 1)
for i in range(N):
    ans[Q[i]] = Q[P[i] - 1]

print(*ans[1:])
