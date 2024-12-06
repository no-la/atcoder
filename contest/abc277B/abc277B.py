N = int(input())
S = [input() for _ in range(N)]

for s in S:
    if s[0] not in "HDCS":
        print("No")
        exit()

for s in S:
    if s[1] not in "A23456789TJQK":
        print("No")
        exit()

for i, s in enumerate(S):
    for j, t in enumerate(S):
        if i != j and s == t:
            print("No")
            exit()

print("Yes")
