n = int(input())

while(n%2 == 0):
    n //= 2
while(n%3 == 0):
    n //= 3
if n == 1:
    ans = "Yes"
else:
    ans = "No"
print(ans)