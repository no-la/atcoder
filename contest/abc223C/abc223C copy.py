N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

t = sum([a/b for a, b in A])/2
print(t)