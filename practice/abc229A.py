s = input()
t = input()
if (s[0]=="." and s[0]==t[1]) or (t[0]=="." and t[0]==s[1]):
    print("No")
else:
    print("Yes")