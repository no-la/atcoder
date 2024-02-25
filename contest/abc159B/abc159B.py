S = input()
N = len(S)
i, j = (N-1)//2, (N+3)//2-1


def f(s):
    n = len(s)
    return ((n%2==0 and s[:n//2]==s[n//2:][::-1]) or
            (n%2==1 and s[:(n-1)//2]==s[(n+1)//2:][::-1]))

print("Yes" if f(S) and f(S[:i]) and f(S[j:]) else "No")