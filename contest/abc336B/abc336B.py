N = int(input())

ans = 0
n = N
while n!=0:
    if n%2 == 0:
        ans += 1
        n //= 2
    else:
        break
print(ans)