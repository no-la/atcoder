N = int(input())
if N>=42:
    N += 1
n = f"000{N}"[-3:]
print("AGC"+n)