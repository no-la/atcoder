X = input()

# 多分そんなに多くないので全探索する

for k in range(len(X), 19):
    # k: 桁数
    for i in range(1, 10):
        # i: 最初の数字
        for d in range(-9, 10):
            # d: 公差
            if i + (k - 1) * d < 0 or i + (k - 1) * d > 9:
                continue
            ans = 0
            for j in range(k):
                ans *= 10
                ans += i + j * d
            if ans >= int(X):
                print(ans)
                exit()
