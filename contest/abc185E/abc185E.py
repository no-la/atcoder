N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

i = 0
ax, bx = 0, 0
while i<min(N, M):
    if A[i]!=-1 and B[i]!=-1 and A[i]==B[i]:
        if N-ax<M-bx:
            B[i] = -1
            bx += 1
        elif N-ax>M-bx:
            A[i] = -1
            ax += 1
        else:
            j = i+1
            while j<min(N, M):
                if A[j]!=-1 and B[j]!=-1 and A[j]==B[j]:
                    if N-ax<M-bx:
                        B[i] = -1
                        bx += 1
                    elif N-ax>M-bx:
                        A[i] = -1
                        ax += 1
                    else:
                        A[i] = -1
                        B[j] = -1
                        ax += 1
                        bx += 1
                    break
                else:
                    j += 1
