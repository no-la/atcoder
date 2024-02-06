N = int(input())
S = [input() for i in range(N)]

ans = {i:0 for i in range(N)}
for i in range(N):
    for j in range(N):
        if S[i][j] == "o":
            ans[i] += 1

ans = sorted(ans.items(), key=lambda x:x[1], reverse=True)

text = ""
for a in ans:
    text += str(a[0]+1) + " "

print(text[:-1])