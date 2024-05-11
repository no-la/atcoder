N, K = map(int, input().split())
A = list(map(int, input().split()))

i = 0
count = 0
remain = K
while i<N:
    if A[i]>remain:
        count += 1
        remain = K
    else:
        remain -= A[i]
        i += 1

if remain<K:
    count += 1

print(count)
