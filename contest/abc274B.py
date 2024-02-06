H, W = map(int, input().split())

ans = [0]*W
for i in range(H):
    l = input()
    for j in range(W):
        if l[j]=="#":
            ans[j] += 1

print(" ".join(map(str, ans)))