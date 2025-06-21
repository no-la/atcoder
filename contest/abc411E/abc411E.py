import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
MOD = 998244353

from collections import defaultdict


# prepare

keys = set()
for l in A:
    for v in l:
        keys.add(v)

value_to_list_indexs = defaultdict(list)
for i, l in enumerate(A):
    for v in l:
        value_to_list_indexs[v].append(i)


keys = sorted(keys)


# dp

dp = defaultdict(int)
# dp[i]: max が i 以下になる場合の数

dp[keys[0] - 1] = 0

count = [0] * N
zero = N


def product(lst):
    res = 1
    for v in lst:
        res *= v
        res %= MOD
    return res


for i, k in enumerate(keys):
    temp = dp[keys[i - 1]] if i > 0 else 1
    for j in value_to_list_indexs[k]:
        if count[j] == 0:
            zero -= 1
        count[j] += 1

        if zero < 0:
            temp *= pow(count[j] - 1, -1, MOD)
            temp *= count[j]
            temp %= MOD

    if zero > 0:
        dp[k] = 0
        continue
    if zero == 0:
        zero = -1
        dp[k] = product(count)
        continue

    dp[k] = temp


case_v = defaultdict(int)
for i, k in enumerate(keys):
    if i == 0:
        case_v[k] = dp[k]
        case_v[k] %= MOD
    else:
        case_v[k] = dp[k] - dp[keys[i - 1]]
        case_v[k] %= MOD


ans = 0
inv = pow(6, -N, MOD)

for k in keys:
    ans += case_v[k] * k
    ans %= MOD

ans *= inv
ans %= MOD
print(ans)
# print(keys, dp, case_v, ans, sep="\n")
