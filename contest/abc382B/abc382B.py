N, D = map(int, input().split())
S = input()
ans = list(S)
count = 0
i = N - 1
while count < D:
    if S[i] == "@":
        ans[i] = "."
        count += 1
    i -= 1
print(*ans, sep="")
