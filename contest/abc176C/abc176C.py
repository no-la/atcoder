N = int(input())
A = list(map(int, input().split()))

pre_max = 0
ans = 0
for a in A:
    if pre_max>a:
        ans += pre_max-a
    else:
        pre_max = a
print(ans)