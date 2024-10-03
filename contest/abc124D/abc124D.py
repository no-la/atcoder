N, K = map(int, input().split())
S = input()

tyokuritu = []
sakadati = []

if S[0] == "0":
    tyokuritu.append(0)
else:
    sakadati.append(0)
for i in range(1, N):
    if S[i] == "0" and S[i - 1] == "1":
        tyokuritu.append(i)
        sakadati.append(i - 1)
    elif S[i] == "1" and S[i - 1] == "0":
        tyokuritu.append(i - 1)
        sakadati.append(i)
if S[N - 1] == "0":
    tyokuritu.append(N - 1)
else:
    sakadati.append(N - 1)

# print(tyokuritu)
# print(sakadati)
