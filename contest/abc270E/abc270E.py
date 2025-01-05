N, K = map(int, input().split())
A = list(map(int, input().split()))

# 全体から何個ずつかを求めてから、あまり分を求める
eated_each = 0
eated_count = 0
remain = N
sorted_A = sorted([(a, i) for i, a in enumerate(A)])
used = [False] * N
for a, i in sorted_A:
    increament = a - eated_each
    if eated_count + remain * increament < K:
        eated_each = a
        eated_count += remain * increament
        remain -= 1
        used[i] = True
    else:
        break

if remain == 0:
    print(*[0] * N)
    exit()

# 残っているremain_count個の中から必要な分を食べる
q, r = divmod(K - eated_count, remain)
eated_each += q
eated_count += q * remain
if eated_count + r != K:
    1 // 0
i = 0
# print(eated_each, eated_count, reamin_count)
while eated_count < K and i < N:
    if not used[i] and A[i] > eated_each:
        eated_count += 1
        A[i] -= 1
    i += 1

ans = [0] * N
for i, a in enumerate(A):
    ans[i] = max(0, a - eated_each)
    if ans[i] > 0 and eated_count < K:
        ans[i] -= 1
        eated_count += 1
print(*ans)
# print(eated_each, A)
