N = int(input())
A = [None] + list(map(int, input().split()))
M = 2**N
d = [None]*(M*N+1)
def f(i):
    if i>=M:
        winner = i%M + 1
        # print("a", winner)
    else:
        j = i<<1
        f(j)
        f(j+1)
        winner = d[j-1] if A[d[j-1]]>A[d[j]] else d[j]
        # print("b", winner)
    d[i-1] = winner
    return

f(1)
# i = 0
# while i<len(d):
#     print(d[i:2*i+1])
#     i = 2*i + 1
print(min((A[d[1]], d[1]), (A[d[2]], d[2]))[1])
