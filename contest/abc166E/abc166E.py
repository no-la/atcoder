N = int(input())
A = list(map(int, input().split()))

# O(N+N+NlogN+N+N) = O(4N+NlogN) = 4*10^6
B = [i+A[i] for i in range(N)]
C = [(j-A[j], j) for j in range(N)]
C.sort()
C0 = [c[0] for c in C]
C1 = [c[1] for c in C]

ans = 0

import bisect
#基本的にbisect_leftを使う
#渡す配列は昇順(reverse=False)ソートしておく

# O(N(logN+logN+logN)) = O(3NlogN) = 10^7
for i in range(N):
    l = bisect.bisect_left(C0, B[i])
    d = bisect.bisect_right(C0[l:], B[i])
    k = bisect.bisect_left(C1[l:], i)
    ans += d - k 

print(ans)