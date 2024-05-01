N = int(input())

b = input()
d = set([b])

for _ in range(N-1):
    w = input()
    if w in d or w[0]!=b[-1]:
        print("No")
        exit()
    b = w
    d.add(w)

print("Yes")
