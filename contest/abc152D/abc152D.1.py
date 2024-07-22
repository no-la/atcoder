N = int(input())
d = [[0]*10 for _ in range(10)]

for i in range(1, N+1):
    l, r = str(i)[0], str(i)[-1]
    l = int(l)
    r = int(r)
    d[l][r] += 1

ans = 0
for i in range(1, N+1):
    l, r = str(i)[0], str(i)[-1]
    l = int(l)
    r = int(r)
    ans += d[r][l]
# print(*d, sep="\n")
print(ans)
