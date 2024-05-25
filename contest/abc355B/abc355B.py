N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

flag = False
ai, bi = 0, 0
while ai<N or bi<M:
    # print(ai, bi)
    if ai==N or (bi<M and A[ai]>B[bi]):
        bi += 1
        flag = False
    else:
        ai += 1
        if flag:
            print("Yes")
            exit()
        flag = True

print("No")
