class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        total, refer = 0, Counter(answers)
        for i in refer:
            total += ((refer[i]-1)//(i+1)+1)*(i+1)
        return total
