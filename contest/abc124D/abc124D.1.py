N, K = map(int, input().split())
S = input()

sakadati = [[0, 0]]

if S[0] == "1":
    sakadati.append([0])
for i in range(1, N):
    if len(sakadati[-1]) == 2:
        sakadati.append([])
    if S[i] != S[i - 1]:
        sakadati[-1].append(i)

if S[N - 1] == "1":
    sakadati[-1].append(N)

while not sakadati[-1]:
    sakadati.pop()

sakadati.append([N, N])


# print(sakadati)

ans = 0
if len(sakadati) <= K:
    ans = sakadati[-1][1] - sakadati[0][0]
else:
    for l in range(len(sakadati) - K):
        r = l + K
        ans = max(ans, sakadati[r][1] - sakadati[l][0])

print(ans)
