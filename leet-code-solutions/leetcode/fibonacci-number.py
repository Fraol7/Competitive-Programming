class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1: return n
        fibo = [0,1]
        while len(fibo) <= n:
            fibo.append(fibo[-1]+fibo[-2])
        return fibo[-1]
        