S = input()
T = input()

c = 0
for s, t in zip(S, T):
    c += not s==t
print(c)