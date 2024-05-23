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
ans = 1
def f(pre):
    global ans
    for i in d[pre]:
        if seen[i]:
            continue
        
        seen[i] = True
        ans += f(i)
        seen[i] = False

        if ans>=10**6:
            print(10**6)
            exit()
    # print(*[i for i in range(N) if seen[i]])
    return

seen[0] = True
f(0)
print(ans)
