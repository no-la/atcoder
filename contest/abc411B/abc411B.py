import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
D = list(map(int, input().split()))
for i in range(N - 1):
    print(*[sum(D[i:j]) for j in range(i + 1, N)])
