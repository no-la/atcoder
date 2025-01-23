N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
X = int(input())

mochi = set(B)

dp = [False] * (X + 1)
# dp[i]: i段目に到達可能かどうか
dp[0] = True

for i in range(X + 1):
    for a in A:
        ni = i + a
        if ni > X:
            break  # Aは単調増加
        if ni in mochi:
            continue
        dp[ni] |= dp[i]

print("Yes" if dp[X] else "No")
