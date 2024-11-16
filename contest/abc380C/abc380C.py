N, K = map(int, input().split())
S = list(input())

d = []
v = S[0]
i = 0
count = 1
while i < N:
    while i < N - 1 and S[i] == S[i + 1]:
        count += 1
        i += 1
    d.append(count)
    count = 1
    i += 1

tar_i = 2 * (K - 1) if S[0] == "1" else 2 * (K - 1) + 1

ans = []
temp = ["0", "1"]
if S[0] == "1":
    temp[0], temp[1] = temp[1], temp[0]

for i in range(tar_i - 1):
    ans.append(temp[i % 2] * d[i])
ans.append("1" * d[tar_i])
ans.append("0" * d[tar_i - 1])
for i in range(tar_i + 1, len(d)):
    ans.append(temp[i % 2] * d[i])

print(*ans, sep="")
