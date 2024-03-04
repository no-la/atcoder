N = int(input())
X = list(map(int, input().split()))

print(min([sum([(x-p)**2 for x in X]) for p in range(1, 101)]))
