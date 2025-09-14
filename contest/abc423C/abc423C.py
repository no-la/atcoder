import sys

input = lambda: sys.stdin.readline().rstrip()

N, R = map(int, input().split())
L = list(map(int, input().split()))


def f(doors, pos):
    op, cl = 0, 0
    m = -1
    for i in range(pos):
        if m == -1 and doors[i] == 0:
            m = i
        else:
            break
        op += doors[i] == 0
        cl += doors[i] == 1

    return op + cl * 2


print(f(L, R) + f(L[::-1], N - R))
