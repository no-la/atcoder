N = int(input())
S = input()

# imos法
imos = [0] * N
for i in range(N):
    imos[i] += int(S[i]) * (i + 1)

for i in range(1, len(imos)):
    imos[i] += imos[i - 1]


# 繰り上がり
for i in range(N - 1, 0, -1):
    q, r = divmod(imos[i], 10)
    imos[i - 1] += q
    imos[i] = r

print(*imos, sep="")
