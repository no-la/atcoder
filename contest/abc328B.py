N = int(input())
D = list(map(int, input().split()))

ans = 0
for i in range(N):
    for d in range(D[i]):
        s = str(i+1) + str(d+1)
        if s == str(i+1)[0]*len(s):
            ans += 1

print(ans)