import sys

input = lambda: sys.stdin.readline().rstrip()
N, M = map(int, input().split())
A = set(map(int, input().split()))

ans = [i for i in range(1, N + 1) if i not in A]
print(len(ans))
print(*ans)
