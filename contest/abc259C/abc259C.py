S = input()
T = input()

if len(T)<len(S):
    print("No")
    exit()
    

ti = 0
for si in range(len(S)):
    if ti>=len(T):
        print("No")
        exit()
    if S[si]==T[ti]:
        ti += 1
        continue
    
    while si>=2 and ti<len(T) and S[si-1]==S[si-2]==T[ti]:
        ti += 1
    
    if S[si]!=T[ti]:
        print("No")
        exit()
        
    ti += 1

print("Yes" if ti==len(T) else "No")
