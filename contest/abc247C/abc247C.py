N = int(input())


# len(Sn) = 2^n - 1
# len(S16) = 2^16 - 1 ~ 7*10^4

def f(n):
    if n==1:
        return "1"
    s = f(n-1)
    return f"{s} {n} {s}"

print(f(N))
