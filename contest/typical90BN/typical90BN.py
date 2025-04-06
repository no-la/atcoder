import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
d = [list(map(int, input().split())) for _ in range(N)]

p = [[0] * N for _ in range(N)]
# p[i][j]: A[i] > A[j] となる確率

for i in range(N):
    il, ir = d[i]
    for j in range(i + 1, N):
        jl, jr = d[j]
        p[i][j] = sum([a > b for a in range(il, ir + 1) for b in range(jl, jr + 1)]) / (
            (ir - il + 1) * (jr - jl + 1)
        )

ans = sum([1 * p[i][j] for i in range(N) for j in range(i + 1, N)])
print(f"{ans:.12f}")
