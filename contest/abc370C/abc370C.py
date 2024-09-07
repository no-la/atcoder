S = input()
T = input()

X = []
def f(s, i):
    if i==len(s):
        return s
    
    if s[i]>T[i]:
        s = s[:i]+T[i]+s[i+1:]
        X.append(s)
        s = f(s, i+1)
    elif s[i]<T[i]:
        s = f(s, i+1)
        s = s[:i]+T[i]+s[i+1:]
        X.append(s)
    else:
        s = f(s, i+1)

    return s

f(S, 0)

print(len(X), *X, sep="\n")    
