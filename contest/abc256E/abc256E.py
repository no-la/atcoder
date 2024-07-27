N = int(input())
X = list(map(int, input().split()))
C = list(map(int, input().split()))

# トポロジカルソート
indeg = [0]*N
for i in range(N):
    indeg[X[i]] += 1


from collections import deque
q = deque([i for i in range(N) if indeg[i]==0])
while q:
    v = q.popleft()
    

