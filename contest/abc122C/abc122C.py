N, Q = map(int, input().split())
S= input()

d = [0]*N
for i in range(1, N):
    if S[i-1:i+1]=="AC":
        d[i] = d[i-1]+1
    else:
        d[i] = d[i-1]

for _ in range(Q):
    l, r = map(int, input().split())
    print(d[r-1]-d[l-1])