class Solution:
    def largestInteger(self, num: int) -> int:
        even, odd = [], []
        num_copy = ""
        for anum in str(num):
            val = int(anum)
            if val%2 == 0:
                even.append(-val)
            else:
                odd.append(-val)
        heapify(even)
        heapify(odd)
        for anum in str(num):
            val = int(anum)
            if val%2 == 0:
                num_copy += str(-heappop(even)) 
            else:
                num_copy += str(-heappop(odd))  
        return int(num_copy)
