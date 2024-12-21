A, B, C = map(int, input().split())

ans = False
ans |= A == B and B == C
ans |= A + B == C
ans |= A == C + B
ans |= A + C == B
print("Yes" if ans else "No")
