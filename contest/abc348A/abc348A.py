N = int(input())
print(*["o" if i%3 else "x" for i in range(1, N+1)], sep="")