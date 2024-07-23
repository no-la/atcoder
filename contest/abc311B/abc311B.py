N, D = map(int, input().split())
S = [input() for _ in range(N)]

def f(i):
    for j in range(N):
        if S[j][i]!="o":
            return False
    return True

ans = 0
c = 0
i = 0
while i<D:
    while i<D and f(i):
        i += 1
        c += 1
    
    ans = max(ans, c)
    c = 0
    i += 1
    
print(ans)
