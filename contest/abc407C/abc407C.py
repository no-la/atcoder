import sys

input = lambda: sys.stdin.readline().rstrip()
S = list(map(int, input()))
N = len(S)
b_count = 0
for i in range(1, N):
    b_count += (S[i - 1] - S[i]) % 10

print(b_count + N + S[-1])
