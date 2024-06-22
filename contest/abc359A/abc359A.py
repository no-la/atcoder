N = int(input())
S = list(input() for _ in range(N))

print(sum([s=="Takahashi" for s in S]))
