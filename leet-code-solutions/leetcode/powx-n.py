class Solution:
    def myPow(self, x: float, n: int) -> float:
        refer = {0:1}
        def helper(x,n,refer):
            if n in refer:
                return refer[n]
            if n == 1:
                refer[1] = x
                return x
            if n == -1:
                refer[-1] = 1/x
                return 1/x
            if n > 1:
                temp = n%2
                refer[n] = ((helper(x, n//2,refer))**2)*(x**temp)
                return refer[n]
            if n < 1:
                temp = n%2
                refer[n] = ((helper(x, (n-1)//2+1,refer))**2)*(x**(-1*temp))
                return refer[n]
        return helper(x,n,refer)
        
