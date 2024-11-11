K = int(input())
S = list(map(lambda x: int(x) - 1, input()[:-1]))
T = list(map(lambda x: int(x) - 1, input()[:-1]))
N = 9

remain = [K] * N
for i in range(4):
    remain[S[i]] -= 1
    remain[T[i]] -= 1


def f(*a):
    rev = 0
    for i in range(N):
        rev += (i + 1) * (10 ** a.count(i))
    return rev


# print(remain)

ans = 0
for i in range(N):
    for j in range(N):
        if remain[i] <= 0 or remain[j] <= 0 or (i == j and remain[i] <= 1):
            continue
        if f(*S, i) > f(*T, j):
            a = remain[i] * (remain[j] - (i == j))
            b = (N * K - 8) * (N * K - 9)
            ans += a / b

print(ans)
