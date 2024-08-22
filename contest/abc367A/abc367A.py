A, B, C = map(int, input().split())

if C<B:
    ans = C<=A<=B
else:
    ans = A<=B or C<=A

print("Yes" if ans else "No")
