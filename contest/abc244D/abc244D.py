S = input().split()
T = input().split()

c = sum([s!=t for s, t in zip(S, T)])
# print(c)

print("Yes" if c!=2 else "No")

