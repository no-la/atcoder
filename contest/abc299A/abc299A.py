N = int(input())
S = input()

start = S.find("|", 0)
end = S.find("|", start + 1)
target = S.find("*")

if start < target and target < end:
    print("in")
else:
    print("out")