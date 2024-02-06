N = int(input())
A, B, AB = [], [], []
for i in range(N):
    a1, b1 = map(int, input().split())
    a = min(a1, b1)
    b = max(a1, b1)
    A.append((a, i))
    B.append((b, i))
    AB.append((a, i, 0))
    AB.append((b, i, 1))

seenA = [0]*N
seenB = [0]*N
seenAB = [0]*N
A.sort()
B.sort()
AB.sort()
for a, i in A:
    seenA[a] = i
for b, i in B:
    seenA[b] = i
        
    