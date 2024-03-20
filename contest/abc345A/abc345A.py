S = input()
if S[0]!="<" or S[-1]!=">":
    print("No")
else:
    print("Yes" if all(s=="=" for s in S[1:-1]) else "No")