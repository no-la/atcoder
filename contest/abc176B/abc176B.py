N = input()
MOD = 9

t = 0
for n in N:
    t = (t+int(n))%MOD
print("Yes" if not t else "No")