X, K = input().split()
K = int(K)
ans = list(map(int, X))[::-1] + [0] * (K - len(X))
for i in range(1, K + 1):
    tar = int("".join(list(map(str, ans[:i]))))
    print(ans[::-1])
    for j in range(K):
        if j < i:
            ans[j] = 0
        elif j == i:
            if tar > 4 * (10 ** (i - 1)):
                ans[i] += 1
            else:
                ...
        else:
            ...

print(int("".join(list(map(str, ans[::-1])))))
