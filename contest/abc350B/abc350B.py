N, Q = map(int, input().split())
T = list(map(lambda x: int(x)-1, input().split()))

d = [1]*N
for i in range(Q):
    d[T[i]] += 1
    
print(sum([a%2 for a in d]))
