X, K = input().split()
K = int(K)
ans = [0] * 20 + list(map(int, X))
ans = ans[::-1]
for i in range(K):
    q, r = divmod(ans[i], 10)
    ans[i + 1] += q
    if r > 4:
        ans[i + 1] += 1
    ans[i] = 0
for i in range(len(ans) - 1):
    q, r = divmod(ans[i], 10)
    ans[i] = r
    ans[i + 1] += q


print(int("".join(list(map(str, ans[::-1])))))
