N, K = map(int, input().split())
A = [int(i) for i in input().split()]

reversed_list = []
for L in range(N):
    for R in range(L, N):
        reversed_list.append(A.copy())
        temp = A[L:R+1]
        temp.reverse()
        #print(L, R, temp)
        reversed_list[-1][L:R+1] = temp
reversed_list.sort()
print(" ".join(map(str, reversed_list[K-1])))