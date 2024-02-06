N = int(input())

m = N
while True:
    if (m//100)*((m%100)//10)==m%10:
        print(m)
        break
    m += 1