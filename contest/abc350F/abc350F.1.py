S = input()
N = len(S)

d = [None]*N
imos = [0]*N

# Find matching parentheses
stack = []
for i in range(N):
    if S[i] == '(':
        stack.append(i)
    elif S[i] == ')':
        j = stack.pop()
        d[i] = j
        d[j] = i

# Update imos array
for i in range(N):
    if d[i] is not None:
        imos[i] = 1
        imos[d[i]] = -1

for i in range(1, N):
    imos[i] += imos[i-1]

ans = []
direction = 1
seen = [False]*N

i = 0
while i < N:
    if seen[i]:
        i += direction
        continue

    if S[i] != '(' and S[i] != ')':
        ans.append(S[i].swapcase() if imos[i] % 2 else S[i])

    j = i
    while d[j] is not None:
        seen[j] = True
        j = d[j]
        direction *= -1

    i = j

print(''.join(ans))
