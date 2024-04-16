N = int(input())
MOD = 10**9+7

if N<2:
    print(0)
    exit()


# (0がない場合) + (9がない場合) - (0と9がない場合)

print((pow(10, N, MOD) - (pow(9, N, MOD)*2 - pow(8, N, MOD)))%MOD)