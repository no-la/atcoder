S = input()
T = input()
for i in range(len(S)):
    if i >= len(T):
        print(i + 1)
        exit()
    if S[i] != T[i]:
        print(i + 1)
        exit()

if len(S) < len(T):
    print(len(S) + 1)
else:
    print(0)
