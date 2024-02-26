N = int(input())
H = list(map(int, input().split()))

b = 0
for i in range(1, N):
    if H[b]<H[i]:
        b = i
    else:
        break
print(H[b])