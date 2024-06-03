A, B, C, D, E, F, X = map(int, input().split())

t = (X//(A+C))*A*B + min(A, (X%(A+C)))*B
a = (X//(D+F))*D*E + min(D, (X%(D+F)))*E
# print(t, a)
if t>a:
    print("Takahashi")
elif t<a:
    print("Aoki")
else:
    print("Draw")
