a, b = map(int, input().split())
print("Yes" if (a+1)%10==b%10 or a%10==(b+1)%10 else "No")