N = int(input())

print(sum([((N//i)*(i*(N//i) + i))//2 for i in range(1, N+1)]))