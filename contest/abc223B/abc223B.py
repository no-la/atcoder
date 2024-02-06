S = input()
n = len(S)
d = [S, S]
for i in range(n):
    d.append(S[n-i-1] + d[-2][:-1])
    d.append(d[-2][1:] + S[i])
d.sort()
print(d[0])
print(d[-1])