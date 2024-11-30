N, M = map(int, input().split())
# 0<=A[0]<=10

ans = []


def f(a, s):
    # print(a, s)
    if len(a) == N:
        ans.append(a.copy())
        return

    i = a[-1] + 10 if a else 1
    while i + 10 * (N - len(a) - 1) <= M:
        a.append(i)
        f(a, s + i)
        a.pop()
        i += 1


f([], 0)
ans.sort()
print(len(ans))
for l in ans:
    print(*l, sep=" ")
