N = int(input())
A = list(map(int, input().split()))

ans = N
i = 0
while True:
    j = i
    while i<N-1 and j<N-1 and A[i+1]-A[i]==A[j+1]-A[j]:
        j += 1
    c = j-i+1
    ans += c*(c-1)//2
    
    # print(i, j, (c*c-c)//2)
    i = j if i<j else j+1
    if i<N:
        ...
    else:
        break

print(ans)
