S = input()
T = input()

if len(T)<len(S):
    print("No")
    exit()

si = 0
ti = 0
while si<len(S) and ti<len(T):
    if S[si]!=T[ti]:
        print("No")
        exit()
    
    s_count = 1
    t_count = 1
    while si+1<len(S) and S[si]==S[si+1]:
        si += 1
        s_count += 1
    while ti+1<len(T) and T[ti]==T[ti+1]:
        ti += 1
        t_count += 1
    
    if s_count>t_count or (s_count==1 and t_count>1):
        print("No")
        exit()
    # print(f"{si=}, {ti=}, {s_count=}, {t_count=}")
    si += 1
    ti += 1

print("Yes" if si==len(S) and ti==len(T) else "No")
    