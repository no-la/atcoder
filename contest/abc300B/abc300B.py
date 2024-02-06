H, W = map(int, input().split())

A = []
B = []


def main():
    for i in range(H):
        A.append(input())
    for i in range(H):
        B.append(input())

    for i in range(W):
        #列の入れ替え
        for j in range(H):
            A[j] = A[j][1:] + A[j][0]

        for k in range(H):
            #行の入れ替え
            temp = A.pop(0)
            A.append(temp)

            #判定
            if judge(A):
                print("Yes")
                return
    print("No")

def judge(a):
    for i in range(H):
        for j in range(W):
            if B[i][j] != a[i][j]:
                return False
    return True

main()