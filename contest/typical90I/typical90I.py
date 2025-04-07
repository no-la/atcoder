import sys, math, bisect

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
d = [list(map(int, input().split())) for _ in range(N)]


def f(x):
    return min(x, 360 - x)


def g(x, y):
    """(x, y)の偏角"""
    return math.degrees(math.atan2(y, x)) % 360


ans = 0
for j in range(N):
    args = []
    for i in range(N):
        if i == j:
            continue
        x = d[i][0] - d[j][0]
        y = d[i][1] - d[j][1]
        a = g(x, y)
        args.append(a)
        # print(f"{j}->{i}", args[-1])

    args.sort()

    for i in range(N - 1):
        x = bisect.bisect_left(args, (args[i] + 180) % 360)
        for k in range(x - 3, x + 3):
            if 0 <= k < N - 1 and k != i:
                ans = max(ans, f(abs(args[i] - args[k])))

print(ans)
