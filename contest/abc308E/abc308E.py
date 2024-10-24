N = int(input())
A = list(map(int, input().split()))
S = input()

# 累積和？
m = [[0] * (N + 1) for _ in range(3)]
e = [[0] * (N + 1) for _ in range(3)]
x = [[0] * (N + 1) for _ in range(3)]
for a, s, i in zip(A, S, range(N)):
    if s == "M":
        m[a][i + 1] += 1
    elif s == "E":
        e[a][i + 1] += 1
    else:
        x[a][i + 1] += 1
    for j in range(3):
        m[j][i + 1] += m[j][i]
        e[j][i + 1] += e[j][i]
        x[j][i + 1] += x[j][i]

# print(m, e, x, sep="\n")


def mex(i, j, k):
    for a in range(10):
        if a != i and a != j and a != k:
            return a


# 真ん中だけ全探索

ans = 0
for i in range(1, N - 1):
    ans += sum(
        [
            mex(a, b, c)
            * (m[a][i] * (e[b][i + 1] - e[b][i]) * (x[c][-1] - x[c][i + 1]))
            for a in range(3)
            for b in range(3)
            for c in range(3)
        ]
    )
    # print(i, ans)

print(ans)
