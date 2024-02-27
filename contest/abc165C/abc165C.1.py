N, M, Q = map(int, input().split())
D = [list(map(int, input().split())) for _ in range(Q)]
# 数列は全部で10H10=92378個
# 各数列に対して得点を求めるのはO(Q)=50
# 合わせるとO(Q*10^5)=5*10^6



# 各数列に対して得点を求める
import itertools
ans = 0
for l in itertools.combinations_with_replacement(range(1, M+1), 10):
    l = sorted(l)
    score = 0
    for a, b, c, d in D:
        if l[b-1]-l[a-1]==c:
            score += d
    ans = max(ans, score)

print(ans)