N, x, y = map(int, input().split())
A = list(map(int, input().split()))

# 縦横（奇数、偶数）を分けて考える

odd = []
even = []
odd.append(set([0]))
even.append(set([0]))
even.append(set([A[0]]))

# 縦を調べる
for i, a in enumerate(A[1::2]):
    odd.append(set())
    for ba in odd[i]:
        odd[-1].add(ba + a)
        odd[-1].add(ba - a)
# 横を調べる
if N > 2:
    for i, a in enumerate(A[2::2]):
        even.append(set())
        for ba in even[i + 1]:
            even[-1].add(ba + a)
            even[-1].add(ba - a)

# print(*odd, "-" * 20, sep="\n")
# print(*even, "-" * 20, sep="\n")
print("Yes" if x in even[-1] and y in odd[-1] else "No")
