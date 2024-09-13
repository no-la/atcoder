N = int(input())
P = list(map(lambda x: int(x)-1, input().split()))

now = N-1
count = 0
while now!=0:
    now = P[now-1]
    count += 1

print(count)
