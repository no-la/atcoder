A, B, N = map(int, input().split())

x = (N//B)*B + N%B
y = ((N//B) - 1)*B + B-1

def f(x):
    if x>N or x<0:
        return 0
    return (A*x)//B - A*(x//B)

print(max(f(x), f(y)))