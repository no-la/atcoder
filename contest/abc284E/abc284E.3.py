import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
from collections import defaultdict
d = defaultdict(list)
for _ in range(M):
    u, v = map(lambda x: int(x)-1, input().split())
    d[u].append(v)
    d[v].append(u)


# 出力するのが min(K, 10^6) なので、全探索してよい？
seen = [0]*N
ans = 0
def f(pre):
    global ans
    
    if ans==10**6:
        return
    
    seen[pre] = True
    ans += 1
    for i in d[pre]:
        if not seen[i]:
            f(i)
    # print(*[i for i in range(N) if seen[i]])
    seen[pre] = False

seen[0] = True
f(0)
print(ans)
