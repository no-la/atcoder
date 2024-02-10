N = int(input())

a = N.bit_length()+1
b = (1<<(a-1)) - N

print(N*a-b-N)