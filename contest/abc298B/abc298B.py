import random

TEST = True


def main():
    global N, A, B, TEST
    if not TEST:
        N = int(input())
        A = [[int(i) for i in input().split()] for n in range(N)]
        B = [[int(i) for i in input().split()] for n in range(N)]
    else:
        test()

    for i in range(3):
        #print(A)
        if judge() == True:
            print("Yes")
            break
        rotate()
    else:
        print("No")
        

def judge():
    global N, A, B
    for i in range(N):
        for j in range(N):
            if A[i][j] == 1 and B[i][j] != 1:
                return False
    return True

def rotate():
    global N, A, B
    temp = [[0 for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            temp[i][j] = A[N-1-j][i]
    A = temp.copy()

def test():
    global N, A, B
    N = random.randrange(1, 5)
    A = [[random.randrange(2) for i in range(N)] for j in range(N)]
    B = [[random.randrange(2) for i in range(N)] for j in range(N)]
    print(f"N = {N}")
    print("A = ")
    for i in range(N):
        print("    "+" ".join(map(str, A[i])))
    print("B = ")
    for i in range(N):
        print("    "+" ".join(map(str, B[i])))
    


main()