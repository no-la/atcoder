N, A, X, Y = map(int, input().split())

# X円で N -> N//A
# Y円で N -> N//b (bはサイコロの出目)

# 順番によらないので、Aをi回選ぶときの金額の期待値を調べればいい

from functools import cache
#メモ化再帰
@cache
def f(n):
    # Yの操作のみでnを0にするまでの金額の期待値
    # f(n) = Y + 1/6 * (f(n) + f(n//2) + ... + f(n//6))
    # 変形して
    # f(n) = 6/5 * Y + 1/5 * (f(n//2) + f(n//3) + ... + f(n//6))
    if n==0:
        return 0
    return 6*Y/5 + sum([f(n//i) for i in range(2, 7)])/5


ans = 10**10
n = N
for i in range(N):
    if n==0:
        ans = min(ans, X*i)
        break
    ans = min(ans, X*i + f(n))
    n //= A
    
print(ans)
