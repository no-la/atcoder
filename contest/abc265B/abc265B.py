import sys

input = lambda: sys.stdin.readline().rstrip()
N, M, T = map(int, input().split())
A = list(map(int, input().split()))
for _ in range(M):
    X, Y = map(int, input().split())
    A[X - 1] -= Y

hp = T

for i in range(N - 1):
    hp -= A[i]
    if hp <= 0:
        print("No")
        exit()

print("Yes")
