N, T = map(int, input().split())
A = list(map(int, input().split()))

hcount = [0]*N
vcount = [0]*N
dcount = [0, 0]

def f(n):
    i = (n-1)//N
    j = (n-1)%N
    return i, j

# print(f(A[0]))
for k, a in enumerate(A):
    i, j = f(a)
    hcount[i] += 1
    vcount[j] += 1
    if i-j==0:
        dcount[0] += 1
    if i+j==N-1:
        dcount[1] += 1

    if hcount[i]==N or vcount[j]==N or max(dcount)==N:
        print(k+1)
        exit()

print(-1)
