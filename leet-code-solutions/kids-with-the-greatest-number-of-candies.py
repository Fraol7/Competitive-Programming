class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest = max(candies)
        result = [True]*len(candies)
        for akid in range(len(candies)):
            if candies[akid] + extraCandies < greatest:
                result[akid] = False
        return result