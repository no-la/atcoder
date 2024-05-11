N = int(input())
A = list(map(int, input().split()))
MOD = 10**8

# 2<= x+y < 10^8 + 10^8
s = sum(A)
A.sort()
ans = 0
import bisect
# 基本的にbisect_leftを使う
# 渡す配列は昇順(reverse=False)ソートしておく
for i in range(N-1):
    a = A[i]
    s -= a
    temp = bisect.bisect_left(A[i+1:], MOD-a)
    # print(a, A[i+1:][:temp], A[i+1:][temp:])
    # print(a, s, N-i-temp-1)
    ans += (N-i-1)*a+s - MOD*(N-i-1-temp)

print(ans)
