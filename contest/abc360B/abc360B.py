S, T = input().split()

for w in range(len(S)):
    for c in range(w):
        if w*len(T)+c<len(S):
            continue
        for i in range(len(T)):
            if w*i+c>=len(S) or S[w*i+c]!=T[i]:
                break
        else:
            print("Yes")
            exit()

print("No")
            
