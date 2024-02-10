"""
メモ化再帰でフィボナッチ数列
"""

class Fib_memo:
    def __init__(self) -> None:
        self.fib_memo = {}
    
    def cal_fib(self, n):
        if n==0 or n==1: # 初項
            self.fib_memo[n] = 1
            return 1

        if n in self.fib_memo: # 既に計算したもの
            return self.fib_memo[n]
        
        self.fib_memo[n] = self.cal_fib(n-1) + self.cal_fib(n-2)
        return self.fib_memo[n]


from functools import cache

@cache
def fib(n):
    return 1 if (n==0 or n==1) else fib(n-1)+fib(n-2)

if __name__ == '__main__':
    import datetime
    fib_memo = Fib_memo()
    t1 = datetime.datetime.now()
    print(fib_memo.cal_fib(200))
    t2 = datetime.datetime.now()
    print(f"----------{t2-t1}----------")
    t1 = datetime.datetime.now()
    print(fib(200))
    t2 = datetime.datetime.now()
    print(f"----------{t2-t1}----------")
    