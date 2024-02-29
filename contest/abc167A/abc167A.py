S = input()
T = input()

print("Yes" if len(S)+1==len(T) and S==T[:-1] else "No")