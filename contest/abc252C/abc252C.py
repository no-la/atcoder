N = int(input())
S = [input() for _ in range(N)]


ans = 1000000000
for i in range(10):
    tar = [0]*10
    for s in S:
        tar[s.index(str(i))] += 1
    m = max(tar)
    for j in range(9, -1, -1):
        if tar[j]==m:
            ans = min(ans, j+(m-1)*10)
            break
print(ans)
    
