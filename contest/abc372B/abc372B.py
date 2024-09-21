import itertools

M = int(input())
x = 3**10

for i in range(M // x, 21):
    # 重複あり組み合わせ O(nHk)=O(n+k-1Ck)
    for l in itertools.combinations_with_replacement(range(11), i):
        if sum([3**a for a in l]) == M:
            print(i)
            print(*l)
            exit()
