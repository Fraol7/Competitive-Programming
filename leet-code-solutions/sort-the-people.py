class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        while True:
            flag = 0
            for i in range(len(heights)-1):
                if heights[i] < heights[i+1]:
                    heights[i], heights[i+1] = heights[i+1], heights[i]
                    names[i], names[i+1] = names[i+1], names[i]
                    flag += 1
            if flag == 0:
                break
        return names
