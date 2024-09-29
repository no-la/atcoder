import itertools

N = int(input())
A = list(map(int, input().split()))

ans = 10**18
# 2^20
for i in range(1, N + 1):
    # 重複なし組み合わせ O(nCk)
    for l in itertools.combinations(range(N), i):
        breakpoints = list(l) + [N]
        # print(breakpoints)
        temp = 0
        now = 0
        li = 0
        for j in range(N):
            if j <= breakpoints[li]:
                now |= A[j]
            else:
                # print(j, now)
                temp ^= now
                li += 1
                now = A[j]
        temp ^= now
        ans = min(ans, temp)


print(ans)
