"""NS"""

N = int(input())

ans = 0
money = 0
tar = [1]
for a in [6, 9]:
    for i in range(1, 100000):
        if a**i > N:
            break
        tar.append(a**i)

tar.sort()
print(tar)

while tar and money < N:
    while tar[-1] + money <= N:
        print(tar[-1])
        money += tar[-1]
        ans += 1
    tar.pop()

print(ans)
