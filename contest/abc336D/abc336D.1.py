# https://atcoder.jp/contests/abc336/submissions/50108598
N = int(input())
A = list(map(int, input().split()))

left = [0]*N # left[i]: i番目を右端する左ピラミッドの長さの最大値
right = [0]*N # right[i]: i番目を左端する右ピラミッドの長さの最大値

# A[_]>=1
left[0] = 1
right[-1] = 1
for i in range(1, N):
    left[i] = min(A[i], left[i-1]+1)
    right[N-i-1] = min(A[N-i-1], right[N-i]+1)


ans = 1
for i in range(N):
    ans = max(ans, min(left[i], right[i]))
print(ans)