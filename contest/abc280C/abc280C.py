S = input()
T = input()

for i in range(len(S)):
    if S[i] != T[i]:
        print(i + 1)
        break
else:
    print(len(S) + 1)
