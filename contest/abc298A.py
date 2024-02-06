def main():
    N = int(input())
    S = input()
    fine = False
    for i in range(N):
        if S[i] == "x":
            break
        if S[i] == "o":
            fine = True
    else:
        if fine:
            print("Yes")
            return
    print("No")

main()