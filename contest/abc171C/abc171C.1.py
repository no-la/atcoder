N = int(input())

d = list("zabcdefghijklmnopqrstuvwxy")
    
def base_n(num_10,n):
    list_n = []
    while num_10:
        list_n.append(num_10%n)
        num_10 //= n
    return list_n[::-1]

print("".join([d[i] for i in base_n(N, 26)]))