N = int(input())
A = list(map(int, input().split()))

d = [[] for _ in range(N + 1)]
for i, a in enumerate(A):
    d[a].append(i)

ans = 0
for ik in d:
    # print(ik)
    for ii in range(len(ik) - 1):
        ki = ii + 1
        i = ik[ii]
        k = ik[ki]
        j_count = k - i - 1
        i_count = ii + 1
        k_count = len(ik) - ki
        # print(i_count, j_count, k_count)
        ans += i_count * j_count * k_count

print(ans)
