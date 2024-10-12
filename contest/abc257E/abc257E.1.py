N = int(input())
C = list(map(int, input().split()))

min_i = -min([(C[i], -i) for i in range(9)])[1]
ans = [min_i + 1] * (N // C[min_i])
cost = (N // C[min_i]) * C[min_i]

# 残っている分で最大化する
for i in range(len(ans)):
    for j in range(9, min_i, -1):
        ncost = cost - C[min_i] + C[j - 1]
        if ncost <= N:
            ans[i] = j
            cost = ncost
            break

print(*ans, sep="")
