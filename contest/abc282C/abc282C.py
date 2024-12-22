N = int(input())
S = list(input())

b = False
for i, s in enumerate(S):
    if not b:
        if s == '"':
            b = True
        elif s == ",":
            S[i] = "."
    else:
        if s == '"':
            b = False

print(*S, sep="")
