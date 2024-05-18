def can_win(A, B):
    from functools import lru_cache
    from collections import defaultdict
    
    N = len(A)
    
    @lru_cache(None)
    def dp(state):
        # 状態をビットマスクとして表現し、各ビットはカードが残っているかどうかを示す
        if state == 0:
            return False
        
        for i in range(N):
            if state & (1 << i):
                for j in range(i + 1, N):
                    if state & (1 << j):
                        if A[i] == A[j] or B[i] == B[j]:
                            new_state = state & ~(1 << i) & ~(1 << j)
                            if not dp(new_state):
                                return True
        return False

    initial_state = (1 << N) - 1
    return dp(initial_state)

N = int(input())
A = []
B = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

if can_win(A, B):
    print("Takahashi")
else:
    print("Aoki")
