S = input()
T = input()
print("Yes" if sum([s!=t for s, t in zip(S, T)])!=2 else "No")
