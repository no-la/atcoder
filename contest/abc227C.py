N = int(input())

ans = 0
for a in range(1, 10**4):
    if a*a*a>N:
        break
    for b in range(a, 10**6):
        if a*b*b>N:
            break
        ans += N//(a*b)-b+1
print(ans)