X, K = input().split()
K = int(K)
ans = [0] * 20 + list(map(int, X))
for i in range(K):
    q, r = divmod(ans[-i - 1], 10)
    ans[-i - 2] += q
    if r > 4:
        ans[-i - 2] += 1
    ans[-i - 1] = 0


print(int("".join(list(map(str, ans)))))
