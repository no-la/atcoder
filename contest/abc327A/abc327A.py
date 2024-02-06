N = int(input())
S = input()

ans = "No"
if "ab" in S or "ba" in S:
    ans = "Yes"
print(ans)