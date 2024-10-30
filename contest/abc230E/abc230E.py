N = int(input())
d = set([0])
for i in range(1, N + 1):
    if i**2 > N:
        break
    if N % i == 0:
        d.add(i)
        d.add(N // i)

d = sorted(d)
# print(d)


ans = 0
for i in range(1, len(d)):
    ans += (d[i] - d[i - 1]) * (N // d[i])
    print(d[i - 1], d[i], N // d[i])

print(ans)
