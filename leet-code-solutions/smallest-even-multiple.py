class Solution:
    def gcd(a,b):
            return gcd(b, a%b)
    def smallestEvenMultiple(self, n: int) -> int:
        return (2*n)//gcd(n,2)
        