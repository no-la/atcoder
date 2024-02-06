S = input()
A = ["A", "B", "C"]
i = 0
for a in A:
    while i<len(S):
        if S[i]!=a:
            break
        i+=1
if i==len(S):
    print("Yes")
else:
    print("No")