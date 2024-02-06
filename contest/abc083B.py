N, A, B = map(int, input().split())
ans = 0
for n in range(1, N+1):
    s = 0
    m = n
    k = len(str(n))
    for i in range(k):
        w = 10**(k-1-i)
        s += m // w
        m %= w
    if A<=s and s<=B:
        ans += n
    # print(n, s)

print(ans)