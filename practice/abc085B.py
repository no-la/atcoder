N = int(input())
D = [int(input()) for i in range(N)]
D.sort()

ans = 1
for i in range(N-1):
    if D[i] == D[i+1]:
        continue
    ans += 1

print(ans)