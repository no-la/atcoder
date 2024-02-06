N = int(input())
cards = list(map(int, input().split()))

cards.sort(reverse=True)
ans = 0
for i in range(N):
    if i%2 == 0:
        ans += cards[i]
    else:
        ans -= cards[i]

print(ans)