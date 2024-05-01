N = int(input())
S = list(input())
Q = int(input())


def f(x):
    return x+N if x<N else x-N


fliped = 0
for _ in range(Q):
    t, a, b = map(int, input().split())
    a -= 1
    b -= 1
    if t==1:
        if fliped:
            a, b = f(a), f(b)
        S[a], S[b] = S[b], S[a]
    else:
        fliped ^= 1

print("".join(S if not fliped else S[N:] + S[:N]))
