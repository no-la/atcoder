N = int(input())
a = [0, 0]
for _ in range(N):
    x, y = map(int, input().split())
    a[0] += x
    a[1] += y

if a[0]>a[1]:
    ans = "Takahashi"
elif a[0]<a[1]:
    ans = "Aoki"
else:
    ans = "Draw"
print(ans)