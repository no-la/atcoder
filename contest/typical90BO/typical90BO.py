import sys

input = lambda: sys.stdin.readline().rstrip()
N, K = input().split()
K = int(K)
N = list(N)


def convert(from_, to, x):
    n = len(x)
    y = sum([from_ ** (n - i - 1) * int(v) for i, v in enumerate(x)])
    if y == 0:
        return [0]
    z = []
    while y > 0:
        q, r = divmod(y, to)
        z.append(r)
        y = q
    return list(reversed(z))


x = N
for _ in range(K):
    x = convert(8, 9, x)
    x = list(map(lambda v: v if v != 8 else 5, x))

print(*x, sep="")
