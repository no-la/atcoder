N = int(input())
S = input()
Q = int(input())

before = [i-1 for i in range(2*N)]
after = [i+1 for i in range(2*N)]
before[0] = None
after[-1] = None

for _ in range(Q):
    t, a, b = map(int, input().split())
    a -= 1
    b -= 1
    print(a, b)
    print(before)
    print(after)
    if t==1: # a<->b
        after[before[b]] = a
        if before[a] is not None:
            after[before[a]] = b
        before[after[a]] = b
        if after[b] is not None:
            before[after[b]] = a
        before[a], before[b] = before[b], before[a]
        after[a], after[b] = after[b], after[a]
    else:
        before[N], before[0] = before[0], before[N]
        after[N-1], after[-1] = after[-1], after[N-1]

print(before)
i = before.index(None)
ans = []
while len(ans)<2*N:
    print(i)
    ans.append(S[i])
    i = after[i]

print(before)
print(after)
print("".join(ans))
