N = int(input())
S = input()
Q = int(input())

before = [i-1 for i in range(2*N)]
after = [i+1 for i in range(2*N)]
before[0] = -1
after[-1] = 2*N

for _ in range(Q):
    t, a, b = map(int, input().split())
    a -= 1
    b -= 1
    if t==1: # a<->b
        after[before[a]], after[before[b]] = after[before[b]], after[before[a]]
        before[a], before[b] = before[b], before[a]
        before[after[a]], before[after[b]] = before[after[b]], before[after[a]]
        after[a], after[b] = after[b], after[a]
    else:
        before[N], before[0] = before[0], before[N]
        after[N-1], after[-1] = after[-1], after[N-1]

        
i = before.index(-1)
ans = []
while len(ans)<2*N:
    print(i)
    ans.append(S[i])
    i = after[i]

print(before)
print(after)
print("".join(ans))
