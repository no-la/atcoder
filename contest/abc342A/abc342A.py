S = input()
s, t = set(S)
print(S.index(s)+1 if S.count(s)==1 else S.index(t)+1)