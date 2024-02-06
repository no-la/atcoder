a, b = map(int, input().split())

ab = a * b
if ab%2 == 0:
    ans = "Even"
else:
    ans = "Odd"

print(ans)