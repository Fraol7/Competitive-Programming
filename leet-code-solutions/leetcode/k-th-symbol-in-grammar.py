class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        if k - 2**(n-2) <= 0:
            return 1 if self.kthGrammar(n-1, k) else 0
        k -= 2**(n-2)
        return 0 if self.kthGrammar(n-1, k) else 1
        
