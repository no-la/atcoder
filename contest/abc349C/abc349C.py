S = input()
T = input()

# TがSの部分列である
# TがSの部分列の末尾にXを追加したものである

S += "X"
c = 0
i = 0
for t in T:
    while i<len(S):
        if t==S[i].capitalize():
            c += 1
            i += 1
            break
        i += 1
print("Yes" if c==3 else "No")