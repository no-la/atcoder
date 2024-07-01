a, b, c = map(int, input().split())
print("Yes" if min(a, c)<=b<=max(a, c) else "No")