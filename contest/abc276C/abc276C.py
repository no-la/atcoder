N = int(input())
P = list(map(int, input().split()))

tail = []
i = N - 1
while i > 0:
    tail.append(P[i])
    if P[i - 1] < P[i]:
        i -= 1
    else:
        break

tar = P[i - 1]
tail.sort(reverse=True)
for t in tail:
    if t < tar:
        tail.remove(t)
        break

ans = P[: i - 1] + [t] + sorted(tail + [tar], reverse=True)
print(*ans)
