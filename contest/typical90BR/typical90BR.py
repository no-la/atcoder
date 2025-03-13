import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
X = []
Y = []
for _ in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)


def f(A):
    A.sort()
    m = A[len(A) // 2]
    m += A[(len(A) - 1) // 2]
    m /= 2
    return int(sum([abs(a - m) for a in A]))


print(f(X) + f(Y))
