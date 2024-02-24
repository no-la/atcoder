N = int(input())
S = input()

import string
D = {char: char for char in string.ascii_lowercase}

Q = int(input())
for _ in range(Q):
    c, d = input().split()
    if c==d:
        continue
    for k in D:
        if D[k]==c:
            D[k] = d

print("".join([D[char] for char in S]))