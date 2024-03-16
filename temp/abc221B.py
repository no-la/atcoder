S = list(input())
T = list(input())

b = False
for i in range(len(S)):
    if S[i]!=T[i]:
        if i==len(S)-1:
            pass
        elif not b:
            S[i], S[i+1] = S[i+1], S[i]
        else:
            print("No")
            exit()
        b = True
print("Yes" if S==T else "No")