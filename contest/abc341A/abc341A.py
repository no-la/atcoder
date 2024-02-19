N = int(input())
print("".join(["0" if i%2==1 else "1" for i in range(2*N+1)]))