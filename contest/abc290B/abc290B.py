N, K = map(int, input().split())
S = input()

count = 0
ans = []
for i, s in enumerate(S):
    if s == "o":
        count += 1
    ans.append(s if count <= K else "x")

print(*ans, sep="")
