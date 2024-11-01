A, B = map(int, input().split())

a1 = [1, 3, 5, 7]
a2 = [2, 3, 6, 7]
a4 = [4, 5, 6, 7]

ans = 0
if A in a1 or B in a1:
    ans += 1
if A in a2 or B in a2:
    ans += 2
if A in a4 or B in a4:
    ans += 4

print(ans)
